from .Window import Window
from Application import Application

class CreateBookWindow(Window):
    def __init__(self) -> None:
        super().__init__("windows/designs/CreateBookWindow.ui")
