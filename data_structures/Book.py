import attr
import logging

from .Recipe import Recipe
from .DataStructure import DataStructure

@attr.s
class Book(DataStructure):
    _title: str = attr.ib(init=False, default="")
    _author: str = attr.ib(init=False, default="")
    _recipies: list = attr.ib(init=False, default=list())

    @property
    def title(self) -> str: return self._title

    @title.setter
    def title(self, title: str) -> None: self._title = title

    @property
    def author(self) -> str: return self._author

    @author.setter
    def author(self, author: str) -> None: self._author = author

    @property
    def recipies(self) -> list: return self._recipies

    @recipies.setter
    def recipies(self, recipies: list) -> None: self._recipies = recipies

    def wrap(self) -> dict:
        data = super().wrap()
        data["title"] = self._title
        data["author"] = self._author
        data["recipies"] = []
        for recipe in self._recipies:
            data["recipies"].append(recipe.wrap())
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._title = data["title"]
        self._author = data["author"]
        self._recipies = []
        for recipe_data in data["recipies"]:
            recipe = Recipe()
            recipe.unwrap(recipe_data)
            self._recipies.append(recipe)

    def save(self):
        data = self.wrap()

        import json
        with open(f"books/{self._title}.json", "w") as file:
            json.dump(data, file, indent=4)
