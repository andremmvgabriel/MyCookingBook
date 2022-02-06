import io
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QPixmap

from windows import Window

import numpy as np
import json

from pdf_generator import PDF, PortraitPDF

from widgets_translators import OptionalDataWidgetTranslator

class OptionalDataWidget(Window):
    __is_collapsed: bool = False
    __max_size: int = 400

    def __init__(self) -> None:
        super().__init__("widgets/designs/OptionalDataWidget.ui", OptionalDataWidgetTranslator())
    
    def setup(self) -> None:
        # Buttons
        self.buttonOptional.clicked.connect(self.toggle_visibility)
        self.buttonAddTag.clicked.connect(self.add_tag)
        self.buttonRemoveTag.clicked.connect(self.remove_tag)
        self.buttonSelectImage.clicked.connect(self.select_image)

        self.buttonAddTag.setEnabled(False)
        self.buttonRemoveTag.setEnabled(False)

        # Entries
        self.entryTag.textChanged.connect(self.tag_text_changed)
        self.entryTag.returnPressed.connect(self.tag_return_key_pressed)
        self.listTags.currentItemChanged.connect(self.tag_selected)

        self.setup_view()
    
    def setup_language(self):
        # Labels
        self.labelAuthor.setText(self._translator.author_label)
        self.labelTags.setText(self._translator.tags_label)
        self.labelDescription.setText(self._translator.description_label)
        
        # Buttons
        self.buttonOptional.setText(self._translator.optional_button)
        self.buttonAddTag.setText(self._translator.add_tag_button)
        self.buttonRemoveTag.setText(self._translator.remove_tag_button)
        self.buttonSelectImage.setText(self._translator.select_image_button)

    def tag_text_changed(self):
        # Get text
        tag_text = self.entryTag.text()

        # Checks button visibility
        if len(tag_text) < 3: self.buttonAddTag.setEnabled(False)
        else: self.buttonAddTag.setEnabled(True)
    
    def tag_return_key_pressed(self):
        # Get text
        tag_text = self.entryTag.text()

        # Checks button visibility
        if len(tag_text) >= 3: self.add_tag()
    
    def tag_selected(self):
        self.buttonRemoveTag.setEnabled(True)
    
    def toggle_visibility(self):
        self.__is_collapsed = not self.__is_collapsed
        self.setup_view()

    def add_tag(self):
        tag = self.entryTag.text()
        tag = tag.capitalize()
        self.entryTag.setText("")
        self.listTags.addItem(tag)

    def remove_tag(self):
        # Gets the item from the list
        row = self.listTags.currentRow()
        item = self.listTags.takeItem(row)

        # Clears the selection
        self.listTags.clearSelection()
        self.listTags.setCurrentRow(999)

        # Deactivates once again the remove button
        self.buttonRemoveTag.setEnabled(False)
    
    def select_image(self):
        file_name = QFileDialog.getOpenFileName(self, "Open file", "", "image files (*.png *.jpg *.icon *.gif)")

        if file_name[0] == "": return

        image = Image.open(file_name[0])
        self.set_image_into_qpixmap(image)
    
    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.frameContents.setHidden(False)

    def show_collapsed(self):
        self.frameContents.setHidden(True)
    
    def open_data(self, data: dict) -> None:
        # Clears
        self.clear()
        
        # Writes
        self.entryAuthor.setText(data["author"])
        self.entryDescription.setText(data["description"])
        for tag in data["tags"]:
            self.listTags.addItem(tag)
        self.set_image_bytes_into_qpixmap(data["image"])
    
    def enter_edit_mode(self):
        self.entryAuthor.setReadOnly(False)
        self.entryDescription.setReadOnly(False)
        self.frameEdit.setHidden(False)
        self.buttonSelectImage.setHidden(False)

    def enter_view_mode(self):
        self.entryAuthor.setReadOnly(True)
        self.entryDescription.setReadOnly(True)
        self.frameEdit.setHidden(True)
        self.buttonSelectImage.setHidden(True)
    
    def get_input_data(self):
        return {
            "author": self.entryAuthor.text(),
            "description": self.entryDescription.toPlainText(),
            "image": self.get_image_bytes_from_qpixmap().decode("latin1"),
            "tags": [self.listTags.item(index).text() for index in range(self.listTags.count())]
        }
    
    def clear(self):
        self.entryAuthor.setText("")
        self.entryDescription.setText("")
        for index in range(self.listTags.count())[::-1]:
            self.listTags.takeItem(index)
        image = Image.open("utils/NoImageIcon.png")
        self.set_image_into_qpixmap(image)
    
    def set_image_into_qpixmap(self, image: Image) -> None:
        image = self.adjust_image_size(image)
        imageqt = ImageQt.ImageQt(image)
        self.labelImage.setPixmap(QPixmap.fromImage(imageqt).copy())
    
    def set_image_bytes_into_qpixmap(self, bytearray: bytes) -> None:
        bytearray_decoded = bytes(bytearray, encoding="latin1")
        bytes_array = QByteArray(bytearray_decoded)
        pix = QPixmap()
        pix.loadFromData(bytes_array, "PNG")
        self.labelImage.setPixmap(pix.copy())

    def get_image_bytes_from_qpixmap(self) -> bytes:
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.OpenModeFlag.WriteOnly)
        self.labelImage.pixmap().save(buff, "PNG")
        return ba.data()
    
    def adjust_image_size(self, image: Image) -> Image:
        width, height = image.size

        if width == height: return image

        new_size = (width if width > height else height, width if width > height else height)
           
        new_image = Image.new(
            "RGB",
            new_size,
            color="white"
        )

        new_image.paste(
            image,
            (
                (new_size[0]-width) // 2,
                (new_size[1]-height) // 2
            )
        )
            
        return new_image.resize((self.__max_size, self.__max_size))
    
    def create_image_from_list(self, list_data: list) -> Image:
        return Image.fromarray( np.array(list_data, dtype="uint8") )
    




    def write_in_pdf(self, pdf: PDF):
        pdf.set_font_size(12)

        init_x = pdf.x
        init_y = pdf.y

        img_y = pdf.y

        pdf.set_font(pdf.font_family, "BU")
        pdf.cell(115, 5, "Tags:", 1, 1, "C")
        pdf.ln(1)

        pdf.set_font(pdf.font_family, "")

        tags_list = str()
        for index in range(self.listTags.count()):
            tag = self.listTags.item(index).text()
            tags_list += f"{tag}; "
        tags_list = tags_list[:-2] + "."
        
        pdf.multi_cell(115, 5, tags_list, 1)

        pdf.ln(3)
        
        init_x = pdf.x
        init_y = pdf.y

        pdf.set_font(pdf.font_family, "BU")
        pdf.cell(115, 5, "Descrição:", 1, 1, "C")
        pdf.ln(1)
        
        pdf.set_font(pdf.font_family, "")

        pdf.multi_cell(115, 5, f"{self.entryDescription.toPlainText()}", 1)

        init_x = pdf.x
        init_y = pdf.y

        pdf.set_xy(130, img_y)
        img = Image.fromqpixmap(self.labelImage.pixmap())
        img.save("temp/img.png")
        pdf.image("temp/img.png", w=70, h=70)
        
        final_x = pdf.x
        final_y = pdf.y

        if final_y > init_y:
            pdf.set_y(final_y)
        else:
            pdf.set_y(init_y)

        pdf.ln(5)
