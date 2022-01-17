from Application import Application
from data_structures.RecipeData import RecipeData
from .Window import Window
from widgets.OptionalDataWidget import OptionalDataWidget
from widgets.ComponentsDataWidget import ComponentsDataWidget
from widgets.IngredientsDataWidget import IngredientsDataWidget
from widgets.StepsDataWidget import StepsDataWidget

from datetime import datetime

class CreateRecipeWindow(Window):
    def __init__(self) -> None:
        self._optional = OptionalDataWidget()
        self._ingredients = IngredientsDataWidget()
        self._steps = StepsDataWidget()
        self._components = ComponentsDataWidget()
        super().__init__("windows/designs/CreateRecipeWindowV4.ui")
    
    def setup(self) -> None:
        # Modules
        self.leftSide.addWidget(self._optional)
        self.leftSide.addWidget(self._ingredients)
        self.leftSide.addWidget(self._steps)
        self.rightSide.addWidget(self._components)

        # Labels
        self.labelRecipeName.setText("Nome da receita:")

        # Buttons
        self.buttonCreate.clicked.connect(self.create_recipe)
        self.buttonCancel.clicked.connect(self.close)
    
    def create_recipe(self):
        recipe = RecipeData()
        recipe.unwrap(self.get_input_data())
        Application.Book.add_recipe(recipe)
        Application.Windows.refresh("book")
        self.close()

    def get_input_data(self):
        data = {}
        data.update({
            "name": self.entryName.text().capitalize(),
            "date": datetime.now().timetuple()
        })
        data.update(self._optional.get_input_data())
        data.update(self._ingredients.get_input_data())
        data.update(self._steps.get_input_data())
        data.update(self._components.get_input_data())
        return data
    
    def clear(self):
        self.entryName.setText("")
        self._optional.clear()
        self._ingredients.clear()
        self._steps.clear()
        self._components.clear()

    def show(self) -> None:
        self.clear()
        self.showMaximized()
