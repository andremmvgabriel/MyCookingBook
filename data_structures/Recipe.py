import attr

from .Component import Component

@attr.s
class Recipe(Component):
    _source: str = attr.ib(init=False, default=None)
    _date: tuple = attr.ib(init=False, default=tuple())
    _tags: list = attr.ib(init=False, default=list())
    _components: list = attr.ib(init=False, default=list())

    @property
    def source(self) -> str: return self._source

    @source.setter
    def source(self, source: str) -> None: self._source = source

    @property
    def date(self) -> tuple: return self._date

    @date.setter
    def date(self, date: tuple) -> None: self._date = date

    @property
    def tags(self) -> list: return self._tags

    @tags.setter
    def tags(self, tags: list) -> None: self._tags = tags

    @property
    def components(self) -> list: return self._components

    @components.setter
    def components(self, components: list) -> None: self._components = components
