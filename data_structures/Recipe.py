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

    def wrap(self) -> dict:
        data = super().wrap()
        data["source"] = self._source
        data["date"] = self._date
        data["tags"] = self._tags
        data["components"] = []
        for component in self._components:
            data["components"].append(component.wrap())
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._source = data["source"]
        self._date = data["date"]
        self._tags = data["tags"]
        self._components = []
        for component_data in data["components"]:
            component = Component()
            component.unwrap(component_data)
            self._components.append(component)
