from typing import List

from .DataStructure import DataStructure

class RecipeComponentData(DataStructure):
    _name: str = ""
    _description: str = ""
    _ingredients: List[str] = list()
    _steps: List[str] = list()

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name: str) -> None: self._name = name

    @property
    def description(self) -> str: return self._description

    @description.setter
    def description(self, description: str) -> None: self._description = description

    @property
    def ingredients(self) -> List[str]: return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: List[str]) -> None: self._ingredients = ingredients

    @property
    def steps(self) -> List[str]: return self._steps

    @steps.setter
    def steps(self, steps: List[str]) -> None: self._steps = steps

    def wrap(self) -> dict:
        data = super().wrap()
        data["name"] = self._name
        data["description"] = self._description,
        data["ingredients"] = self._ingredients,
        data["steps"] = self._steps
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._name = data["name"]
        self._description = data["description"]
        self._ingredients = data["ingredients"]
        self._steps = data["steps"]
