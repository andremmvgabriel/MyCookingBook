import logging
from pathlib import Path
from .Window import Window
from Application import Application

class MainWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/MainWindow.ui")
    
    # Overridable Functions
    def setup(self) -> None:
        # Title
        self.labelTitle.setText("Os Meus Livros de Receitas")

        # Buttons
        self.buttonOpen.clicked.connect(self.open_book)
        self.buttonOpen.setEnabled(False)
        self.buttonOpen.setText("Abrir")
        self.buttonCreate.clicked.connect(self.create_book)
        self.buttonImport.clicked.connect(self.import_book)

        # Dropbox
        self.entryBook.currentIndexChanged.connect(self.book_selected)
    
    def refresh(self) -> None:
        self.entryBook.clear()

        # Dropbox
        
        for book_path in Path(Application.get_books_path()).glob("*.json"):
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
        pass

    def book_selected(self):
        book_name = self.entryBook.currentText()
        self.buttonOpen.setEnabled(True if len(book_name) != 0 else False)
