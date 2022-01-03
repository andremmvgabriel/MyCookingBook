import attr

@attr.s
class DataStructure:
    def wrap(self) -> dict: return {}
    def unwrap(self, data: dict) -> None: assert isinstance(data, dict)
