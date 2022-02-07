from utils import Window
from data_structures import RecipeData
from Application import Application

from pdf_generator import PDF

class RecipeCard(Window):
    def __init__(self, recipe: RecipeData) -> None:
        self._recipe = recipe
        super().__init__("widgets/designs/RecipeCardWidget.ui")
    
    def setup(self) -> None:
        # Buttons
        self.buttonName.setText(self._recipe.name)
        self.buttonName.clicked.connect(self.open_recipe)

    def open_recipe(self):
        Application.Windows.get("recipe").open_recipe(self._recipe)
        Application.Windows.open("recipe")
        Application.Windows.close("book")
    
    def write_in_pdf(self, pdf: PDF):
        Application.Windows.get("recipe").open_recipe(self._recipe)
        Application.Windows.get("recipe").write_in_pdf(pdf)
