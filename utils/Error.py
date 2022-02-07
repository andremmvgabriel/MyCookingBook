class Error:
    _code: int = 0
    _reason: str = 0
    _tag: str = ""

    @property
    def code(self) -> int: return self._code

    @property
    def reason(self) -> str: return self._reason

    @property
    def tag(self) -> str: return self._tag

    def __init__(self, code: int, reason: str, tag: str = "") -> None:
        self._code = code
        self._reason = reason
        self._tag = tag
