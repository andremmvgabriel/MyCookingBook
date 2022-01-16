import sys
from PyQt5 import QtWidgets
from widgets import SectionWidget
from widgets.OptionalDataWidget import OptionalDataWidget
from windows.CreateRecipeWindow import CreateRecipeWindow

app = QtWidgets.QApplication(sys.argv)

#uut = SectionWidget("My Testing!")
#uut = OptionalDataWidget()
#uut.show()
#uut.showMaximized()

uut = CreateRecipeWindow()
#uut.show()
uut.showMaximized()

app.exec_()