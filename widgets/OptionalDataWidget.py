import io
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QPixmap

from windows import Window

class OptionalDataWidget(Window):
    __is_collapsed: bool = False

    def __init__(self) -> None:
        super().__init__("widgets/designs/OptionalDataWidget.ui")
    
    def setup(self) -> None:
        # Buttons
        self.buttonOptional.setText("Opcional")
        self.buttonOptional.clicked.connect(self.toggle_visibility)
        self.buttonAddTag.setText("Adicionar")
        self.buttonAddTag.clicked.connect(self.add_tag)
        self.buttonRemoveTag.setText("Remover")
        self.buttonRemoveTag.clicked.connect(self.remove_tag)
        self.buttonSelectImage.setText("Selecionar imagem")
        self.buttonSelectImage.clicked.connect(self.select_image)

        self.buttonAddTag.setEnabled(False)
        self.buttonRemoveTag.setEnabled(False)

        # Entries
        self.entryTag.textChanged.connect(self.tag_text_changed)
        self.entryTag.returnPressed.connect(self.tag_return_key_pressed)
        self.listTags.currentItemChanged.connect(self.tag_selected)

        self.setup_view()

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

        self.set_image_file_into_qpixmap(file_name[0])
    
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
        self.set_image_file_into_qpixmap("utils/NoImageIcon.png")
    
    def set_image_file_into_qpixmap(self, path: str) -> None:
        #self.labelImage.setPixmap(QPixmap(path).copy())

        image = Image.open(path)
        #image = image.resize((self.labelImage.maximumWidth(), self.labelImage.maximumHeight()))
        imageqt = ImageQt.ImageQt(image)
        self.labelImage.setPixmap(QPixmap.fromImage(imageqt).copy())
    
    def set_image_bytes_into_qpixmap(self, bytearray: bytes) -> None:
        #bytearray = bytes(bytearray, encoding="latin1")
        #image = Image.open(io.BytesIO(bytearray))
        #imageqt = ImageQt.ImageQt(image)
        #self.labelImage.setPixmap(QPixmap.fromImage(imageqt).copy())
        
        bytearray = bytes(bytearray, encoding="latin1")
        bytes_array = QByteArray(bytearray)
        pix = QPixmap()
        pix.loadFromData(bytes_array, "PNG")
        self.labelImage.setPixmap(pix.copy())
    
    def get_image_bytes_from_qpixmap(self) -> bytes:
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.OpenModeFlag.WriteOnly)
        self.labelImage.pixmap().save(buff, "PNG")
        return ba.data()
