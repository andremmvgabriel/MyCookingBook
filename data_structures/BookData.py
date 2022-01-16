import logging

from typing import List

from .RecipeData import RecipeData
from .DataStructure import DataStructure

class BookData(DataStructure):
    _name: str = ""
    _author: str = ""
    _recipies: List[RecipeData] = list()
    _tags: List[str] = list()
    _date: tuple = tuple()
    __valid: bool = True

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name: str) -> None: self._name = name

    @property
    def author(self) -> str: return self._author

    @author.setter
    def author(self, author: str) -> None: self._author = author

    @property
    def recipies(self) -> List[RecipeData]: return self._recipies

    @recipies.setter
    def recipies(self, recipies: List[RecipeData]) -> None: self._recipies = recipies

    @property
    def tags(self) -> List[str]: return self._tags

    @tags.setter
    def tags(self, tags: List[str]) -> None: self._tags = tags

    @property
    def date(self) -> tuple: return self._date

    @date.setter
    def date(self, date: tuple) -> None: self._date = date

    @property
    def valid(self) -> bool: return self.__valid

    def wrap(self) -> dict:
        data = super().wrap()
        data["name"] = self._name
        data["author"] = self._author
        data["recipies"] = []
        for recipe in self._recipies:
            data["recipies"].append(recipe.wrap())
        data["tags"] = self._tags
        data["date"] = self._date
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._name = data["name"]
        self._author = data["author"]
        self._recipies = []
        for recipe_data in data["recipies"]:
            recipe = RecipeData()
            recipe.unwrap(recipe_data)
            self._recipies.append(recipe)
        self._tags = data["tags"]
        self._date = data["date"]
        print()
