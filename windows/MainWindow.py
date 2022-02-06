import json
import logging
from pathlib import Path
from .Window import Window
from Application import Application
from windows_translators import MainWindowTranslator

from PyQt5.QtWidgets import QFileDialog

class MainWindow(Window):
    __languages_list: list = [
        "English",
        "Portuguese"
    ]

    def __init__(self) -> None:
        super().__init__("windows/designs/MainWindow.ui", MainWindowTranslator())
    
    # Overridable Functions
    def setup(self) -> None:
        # Buttons
        self.buttonOpen.clicked.connect(self.open_book)
        self.buttonOpen.setEnabled(False)
        self.buttonCreate.clicked.connect(self.create_book)
        self.buttonImport.clicked.connect(self.import_book)
        self.buttonMoreOptions.clicked.connect(self.open_options)

        # Dropbox
        self.entryBook.currentIndexChanged.connect(self.book_selected)
        self.entryLanguage.currentIndexChanged.connect(self.change_language)
        self.entryLanguage.setCurrentIndex(self.__languages_list.index(Application.language))
    
    def setup_language(self):
        # Labels
        self.labelTitle.setText(self._translator.title_label)
        self.labelLanguage.setText(self._translator.language_label)

        # Buttons
        self.buttonOpen.setText(self._translator.open_button)
        self.buttonCreate.setText(self._translator.create_button)
        self.buttonImport.setText(self._translator.import_button)
        self.buttonMoreOptions.setText(self._translator.options_button)

        # Dropbox
        for index in range(self.entryLanguage.count()):
            self.entryLanguage.setItemText(
                index,
                self._translator.language_dropbox[index]
            )
    
    def refresh(self) -> None:
        self.entryBook.clear()

        # Dropbox
        
        for book_path in Path(Application.books_path).glob("*.json"):
            book_name = book_path.parts[-1].split(".")[0]
            self.entryBook.addItem(book_name)
        
        self.entryBook.setCurrentIndex(-1)
    
    # Callbacks
    def open_book(self):
        book_name = self.entryBook.currentText()
        Application.Book.open(book_name)
        Application.Windows.open("book")
        self.close()
    
    def create_book(self):
        Application.Windows.open("create_book")
    
    def import_book(self):
        file_name = QFileDialog.getOpenFileName(self, "Open file", "", "book files (*.json)")

        if file_name[0] == "": return

        try:
            with open(file_name[0], "r") as file:
                data = json.load(file)
                # TODO - Complete method
            
        except json.JSONDecodeError:
            print("Incorrect file format.")

    def book_selected(self):
        book_name = self.entryBook.currentText()
        self.buttonOpen.setEnabled(True if len(book_name) != 0 else False)
    
    def change_language(self):
        Application.language = self.__languages_list[self.entryLanguage.currentIndex()]
        Application._save_configurations()
        Application.setup_language()
    
    def open_options(self):
        Application.Windows.open("options")
