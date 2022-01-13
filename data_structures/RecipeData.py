from typing import List

from .RecipeComponentData import RecipeComponentData

class RecipeData(RecipeComponentData):
    _author: str = ""
    _tags: List[str] = list()
    _date: tuple = tuple()    
    _components: List[RecipeComponentData] = list()

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
        data["author"] = self._author
        data["date"] = self._date
        data["tags"] = self._tags
        data["components"] = []
        for component in self._components:
            data["components"].append(component.wrap())
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._author = data["author"]
        self._date = data["date"]
        self._tags = data["tags"]
        self._components = []
        for component_data in data["components"]:
            component = RecipeComponentData()
            component.unwrap(component_data)
            self._components.append(component)
