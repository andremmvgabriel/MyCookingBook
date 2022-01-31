from PyQt5 import QtWidgets, uic, QtCore, QtGui

from utils import Translator

class Window(QtWidgets.QWidget):
    _translator: Translator
    
    def __init__(self, ui_file: str, translator: Translator = None) -> None:
        super(Window, self).__init__()
        uic.loadUi(ui_file, self)
        self._translator = translator
        self.setup()

    # Overridable functions
    def setup(self) -> None: pass
    def refresh(self) -> None: pass

    #def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
    #    print(self.width(), self.height())
    #    super().resizeEvent(a0)
        
