from typing import List

from .DataStructure import DataStructure

class IngredientsData(DataStructure):
    _ingredients: List[str]

    @property
    def ingredients(self) -> List[str]: return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: List[str]) -> None: self._ingredients = ingredients

    def wrap(self) -> dict:
        data = super().wrap()
        data["ingredients"] = self._ingredients
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._ingredients = data["ingredients"]
