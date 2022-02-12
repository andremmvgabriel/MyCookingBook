import logging
from data_structures import BookData
from utils import Window
from Application import Application, BookSaveError

from windows_translators import CreateBookWindowTranslator

class CreateBookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/CreateBookWindow.ui", CreateBookWindowTranslator())
    
    def show(self) -> None:
        self.entryTitle.setText("")
        self.entryAuthor.setText("")
        return super().show()
    
    # Overridable 
    def setup(self) -> None:
        # Buttons
        self.buttonCreate.clicked.connect(self.create_book)
        self.buttonCancel.clicked.connect(self.close)
    
    def setup_language(self) -> None:
        # Labels
        self.labelRequiredInfo.setText(self._translator.required_info_label)
        self.labelTitle.setText(self._translator.title_label)
        self.labelAuthor.setText(self._translator.author_label)

        # Buttons
        self.buttonCreate.setText(self._translator.create_button)
        self.buttonCancel.setText(self._translator.cancel_button)
    
    # Callbacks
    def create_book(self) -> None:
        book_data = self.get_inputs()
        try:
            Application.Book.create(book_data)
            Application.Windows.refresh("main")
            self.close()
        except BookSaveError:
            logging.warning("The new book inserted data is invalid.")

    #
    def get_inputs(self) -> BookData:
        book_data = BookData()
        book_data.name = self.entryTitle.text()
        book_data.author = self.entryAuthor.text()
        return book_data