import logging
from data_structures import BookData
from .Window import Window
from Application import Application, BookSaveError

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
        book_data = self.get_inputs()
        try:
            Application.Book.create(book_data)
            self.close()
        except BookSaveError:
            logging.warning("The new book inserted data is invalid.")

    #
    def get_inputs(self) -> BookData:
        book_data = BookData()
        book_data.title = self.entryTitle.text()
        book_data.author = self.entryAuthor.text()
        return book_data