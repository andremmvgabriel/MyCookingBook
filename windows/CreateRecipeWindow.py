from datetime import datetime

from Application import Application
from data_structures.RecipeData import RecipeData
from .Window import Window
from widgets.OptionalDataWidget import OptionalDataWidget
from widgets.ComponentsDataWidget import ComponentsDataWidget
from widgets.IngredientsDataWidget import IngredientsDataWidget
from widgets.StepsDataWidget import StepsDataWidget

from windows_translators import CreateRecipeWindowTranslator

class CreateRecipeWindow(Window):
    def __init__(self) -> None:
        self._optional = OptionalDataWidget()
        self._ingredients = IngredientsDataWidget()
        self._steps = StepsDataWidget()
        self._components = ComponentsDataWidget()
        super().__init__("windows/designs/CreateRecipeWindow.ui", CreateRecipeWindowTranslator())
    
    def setup(self) -> None:
        # Modules
        self.leftSide.addWidget(self._optional)
        self.leftSide.addWidget(self._ingredients)
        self.leftSide.addWidget(self._steps)
        self.rightSide.addWidget(self._components)

        # Buttons
        self.buttonCreate.clicked.connect(self.create_recipe)
        self.buttonCancel.clicked.connect(self.close)
    
    def setup_language(self) -> None:
        # Labels
        self.labelRecipeName.setText(f"{self._translator.recipe_name_label}:")

        # Buttons
        self.buttonCreate.setText(self._translator.create_button)
        self.buttonCancel.setText(self._translator.cancel_button)

        # Line edits
        self.entryName.setPlaceholderText(self._translator.name_placeholder_entry)

        # Modules
        self._optional.setup_language()
        self._ingredients.setup_language()
        self._steps.setup_language()
        self._components.setup_language()
    
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
