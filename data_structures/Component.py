import attr

from .DataStructure import DataStructure

@attr.s
class Component(DataStructure):
    _name: str = attr.ib(init=False, default="")
    _description: str = attr.ib(init=False, default=None)
    #_image: 
    _ingredients: list = attr.ib(init=False, default=list())
    _steps: list = attr.ib(init=False, default=list())

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name: str) -> None: self._name = name

    @property
    def description(self) -> str: return self._description

    @description.setter
    def description(self, description: str) -> None: self._description = description

    #def image(self)

    @property
    def ingredients(self) -> list: return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list) -> None: self._ingredients = ingredients

    @property
    def steps(self) -> list: return self._steps

    @steps.setter
    def steps(self, steps: list) -> None: self._steps = steps

    def wrap(self) -> dict:
        data = super().wrap()
        data["name"] = self._name
        data["description"] = self._description,
        data["ingredients"] = self._ingredients,
        data["steps"] = self._steps
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap()
        self._name = data["name"]
        self._description = data["description"]
        self._ingredients = data["ingredients"]
        self._steps = data["steps"]
