import sys
from PyQt5 import QtWidgets
from windows.CreateRecipeWindow import CreateRecipeWindow

app = QtWidgets.QApplication(sys.argv)

uut = CreateRecipeWindow()
#uut.show()
uut.showMaximized()

app.exec_()