from PyQt5 import QtWidgets, uic, QtCore, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self, ui_file: str) -> None:
        super(Window, self).__init__()
        uic.loadUi(ui_file, self)
        self.setup()

    # Overridable functions
    def setup(self) -> None: pass
    def refresh(self) -> None: pass

    #def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
    #    print(self.width(), self.height())
    #    super().resizeEvent(a0)
        
