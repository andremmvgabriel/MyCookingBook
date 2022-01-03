from data_structures import Book
from .Window import Window
from Application import Application

class CreateBookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/CreateBookWindow.ui")
    
    # Overridable 
    def setup(self) -> None:
        # Labels
        self.labelTitle.setText("Título")
        self.labelAuthor.setText("Autor")

        # Buttons
        self.buttonCreate.clicked.connect(self.create_book)
        self.buttonCancel.clicked.connect(self.close)
    
    # Callbacks
    def create_book(self) -> None:
        book = self.get_inputs()
        if self.validate_inputs(book):
            book.save()
            self.close()

    #
    def get_inputs(self) -> Book:
        book = Book()
        book.title = self.entryTitle.text()
        book.author = self.entryAuthor.text()
        return book

    def validate_inputs(self, book: Book) -> bool:
        return True