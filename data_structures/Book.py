import attr
import logging

@attr.s
class Book:
    _title: str = attr.ib(init=False, default="")
    _author: str = attr.ib(init=False, default="")

    @property
    def title(self) -> str: return self._title

    @title.setter
    def title(self, title: str) -> None: self._title = title

    @property
    def author(self) -> str: return self._author

    @author.setter
    def author(self, author: str) -> None: self._author = author

    def save(self):
        data = {
            "title": self._title,
            "author": self._author
        }

        import json
        with open(f"books/{self._title}.json", "w") as file:
            json.dump(data, file, indent=4)
