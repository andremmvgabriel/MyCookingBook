from .DataStructure import DataStructure
from .IngredientsData import IngredientsData
from .StepsData import StepsData

class ComponentData(DataStructure):
    _name: str
    _ingredients: IngredientsData
    _steps: StepsData

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name: str) -> None: self._name = name

    @property
    def ingredients(self) -> IngredientsData: return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: IngredientsData) -> None: self._ingredients = ingredients

    @property
    def steps(self) -> StepsData: return self._steps

    @steps.setter
    def steps(self, steps: StepsData) -> None: self._steps = steps

    def wrap(self) -> dict:
        data = super().wrap()
        data.update(self._ingredients.wrap())
        data.update(self._steps.wrap())
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._ingredients.unwrap(data)
        self._steps.unwrap(data)
