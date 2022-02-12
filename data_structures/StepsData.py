from typing import List

from .DataStructure import DataStructure

class StepsData(DataStructure):
    _steps: List[str]

    @property
    def steps(self) -> List[str]: return self._steps

    @steps.setter
    def steps(self, steps: List[str]) -> None: self._steps = steps

    def wrap(self) -> dict:
        data = super().wrap()
        data["steps"] = self._steps
        return data
    
    def unwrap(self, data: dict) -> None:
        super().unwrap(data)
        self._steps = data["steps"]
