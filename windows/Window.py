from PyQt5 import QtWidgets, uic

class Window(QtWidgets.QWidget):
    def __init__(self, ui_file: str) -> None:
        super(Window, self).__init__()
        uic.loadUi(ui_file, self)
