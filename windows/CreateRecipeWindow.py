from .Window import Window
from widgets.OptionalDataWidget import OptionalDataWidget
from widgets.ComponentsDataWidget import ComponentsDataWidget
from widgets.IngredientsDataWidget import IngredientsDataWidget
from widgets.StepsDataWidget import StepsDataWidget

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

        # Buttons
        self.buttonCreate.clicked.connect(self.create_recipe)
        self.buttonCancel.clicked.connect(self.close)
    
    def create_recipe(self):
        print(self.get_input_data())

    def get_input_data(self):
        data = {}
        data.update(self._optional.get_input_data())
        data.update(self._ingredients.get_input_data())
        data.update(self._steps.get_input_data())
        data.update(self._components.get_input_data())
        return data
