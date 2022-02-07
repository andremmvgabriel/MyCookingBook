from PyQt5 import QtWidgets
from urllib3 import Retry

from Application import Application

from utils import Window

from windows_translators import OptionsWindowTranslator

class OptionsWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/OptionsWindow.ui", OptionsWindowTranslator())
    
    def show(self) -> None:
        # Line edits
        self.entryPDFs.setText(Application.pdfs_path)
        self.entryBooks.setText(Application.books_path)
        return super().show()
    
    def setup(self) -> None:
        # Buttons
        self.buttonPDFs.clicked.connect(self.select_pdfs_directory)
        self.buttonBooks.clicked.connect(self.select_books_directory)
        self.buttonSave.clicked.connect(self.save)
        self.buttonCancel.clicked.connect(self.close)
    
    def setup_language(self):
        # Labels
        self.labelPDFs.setText(self._translator.pdfs_label)
        self.labelBooks.setText(self._translator.books_label)

        # Buttons
        self.buttonPDFs.setText(self._translator.pdfs_button)
        self.buttonBooks.setText(self._translator.books_button)
        self.buttonSave.setText(self._translator.save_button)
        self.buttonCancel.setText(self._translator.cancel_button)
    
    def select_pdfs_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, self._translator.pdfs_select_dir)
        if len(directory) != 0: self.entryPDFs.setText(directory)

    def select_books_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, self._translator.books_select_dir)
        if len(directory) != 0: self.entryBooks.setText(directory)

    def save(self):
        Application.pdfs_path = self.entryPDFs.text()
        Application.books_path = self.entryBooks.text()
        Application._save_configurations()
        Application.Windows.refresh("main")
        self.close()
