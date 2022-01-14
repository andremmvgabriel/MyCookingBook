from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from windows import Window

class OptionalDataWidget(Window):
    __is_collapsed: bool = True

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
    
    def setup_view(self):
        if self.__is_collapsed: self.show_collapsed()
        else: self.show_expanded()
    
    def show_expanded(self):
        self.contentOptional.setHidden(False)

    def show_collapsed(self):
        self.contentOptional.setHidden(True)
    
    def get_input_data(self):
        return {
            "author": self.entryAuthor.text(),
            "description": self.entryDescription.toPlainText(),
            "tags": [self.listTags.item(index).text() for index in range(self.listTags.count() - 1)]
        }
