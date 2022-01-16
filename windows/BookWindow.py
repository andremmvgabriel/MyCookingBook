import json
from Application import Application

from .Window import Window

class BookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/BookWindow.ui")
    
    def setup(self) -> None:
        # Labels

        # Buttons
        self.buttonCreateRecipe.clicked.connect(self.create_recipe)
    
    def create_recipe(self) -> None:
        Application.Windows.open("create_recipe")
    
    def refresh(self): pass
