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
        pass

    # 
    def validate_inputs(self) -> None:
        pass