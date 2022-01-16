from typing import List

from .DataStructure import DataStructure
from .RecipeComponentData import RecipeComponentData

class RecipeData(DataStructure):
    _name: str = ""
    _author: str = ""
    _description: str = ""
    _tags: List[str] = list()
    _ingredients: List[str] = list()
    _steps: List[str] = list()
    _date: tuple = tuple()
    _components: List[RecipeComponentData] = list()

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

    @property
    def author(self) -> str: return self._author

    @author.setter
    def author(self, author: str) -> None: self._author = author

    @property
    def tags(self) -> list: return self._tags

    @tags.setter
    def tags(self, tags: list) -> None: self._tags = tags

    @property
    def date(self) -> tuple: return self._date

    @date.setter
    def date(self, date: tuple) -> None: self._date = date

    @property
    def components(self) -> List[RecipeComponentData]: return self._components

    @components.setter
    def components(self, components: List[RecipeComponentData]) -> None: self._components = components

    def wrap(self) -> dict:
        data = super().wrap()
        data["name"] = self._name
        data["description"] = self._description
        data["ingredients"] = self._ingredients
        data["steps"] = self._steps
        data["author"] = self._author
        data["date"] = self._date
        data["tags"] = self._tags
        data["components"] = []
        for component in self._components:
            data["components"].append(component.wrap())
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._name = data["name"]
        self._description = data["description"]
        self._ingredients = data["ingredients"]
        self._steps = data["steps"]
        self._author = data["author"]
        self._date = data["date"]
        self._tags = data["tags"]
        self._components = []
        for component_data in data["components"]:
            component = RecipeComponentData()
            component.unwrap(component_data)
            self._components.append(component)
