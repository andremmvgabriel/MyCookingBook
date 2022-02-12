from typing import List

from .DataStructure import DataStructure

class Optionaldata(DataStructure):
    _author: str
    _tags: List[str]
    _description: str
    _image: bytes

    @property
    def author(self) -> str: return self._author

    @author.setter
    def author(self, author: str) -> None: self._author = author

    @property
    def tags(self) -> List[str]: return self._tags

    @tags.setter
    def tags(self, tags: List[str]) -> None: self._tags = tags

    @property
    def description(self) -> str: return self._description

    @description.setter
    def description(self, description: str) -> None: self._description = description

    @property
    def image(self) -> bytes: return self._image

    @image.setter
    def image(self, image: bytes) -> None: self._image = image

    def wrap(self) -> dict:
        data = super().wrap()
        data["author"] = self._author
        data["tags"] = self._tags
        data["description"] = self._description
        data["image"] = self._image
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)

        self._author = data["author"]
        self._tags = data["tags"]
        self._description = data["description"]
        self._image = data["image"]
