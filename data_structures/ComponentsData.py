from typing import List

from .DataStructure import DataStructure
from .ComponentData import ComponentData

class ComponentsData(DataStructure):
    _components: List[ComponentData]

    @property
    def components(self) -> List[ComponentData]: return self._components

    @components.setter
    def components(self, components: List[ComponentData]) -> None: self._components = components

    def wrap(self) -> dict:
        data = super().wrap()
        data["components"] = [component.wrap() for component in self._components]
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        for component_data in data["components"]:
            component = ComponentData()
            component.unwrap(component_data)
            self._components.append(component)
