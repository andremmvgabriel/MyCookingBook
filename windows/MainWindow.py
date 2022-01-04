from pathlib import Path
from .Window import Window
from Application import Application

class MainWindow(Window):
    __books_path: Path = Path("books")

    def __init__(self) -> None:
        super().__init__("windows/designs/MainWindow.ui")
        self.__books_path.mkdir(exist_ok=True)
    
    # Overridable Functions
    def setup(self) -> None:
        # Title
        self.labelTitle.setText("Os Meus Livros de Receitas")

        # Buttons
        self.buttonOpen.clicked.connect(self.open_book)
        self.buttonOpen.setText("Abrir")
        self.buttonCreate.clicked.connect(self.create_book)
        self.buttonImport.clicked.connect(self.import_book)

        # Dropbox
        self.entryBook.currentIndexChanged.connect(self.book_selected)

        from PyQt5 import QtWidgets
        #QtWidgets.QLabel().setTe
        self.refresh()
    
    def refresh(self) -> None:
        # Dropbox
        for book_path in self.__books_path.glob("*.json"):
            book_name = book_path.parts[-1].split(".")[0]
            self.entryBook.addItem(book_name)
        
        self.entryBook.setCurrentIndex(-1)
    
    # Callbacks
    def open_book(self):
        Application.Windows.open("book")
        self.close()
    
    def create_book(self):
        Application.Windows.open("create_book")
    
    def import_book(self):
        pass

    def book_selected(self):
        pass

