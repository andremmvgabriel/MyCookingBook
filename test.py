import sys
import json
import numpy as np
from PIL import Image, ImageQt

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

image = Image.open("utils/NoImageIcon.png")
#image.show()

array = np.array(image)
print(array[0][:10])

array_list = array.tolist()
print(array_list[0][:50])

dict_1 = {
    "image": array_list
}

with open("test_list.json", "w") as file:
    json.dump(dict_1, file)

with open("test_list.json", "r") as file:
    data_from_json = json.load(file)

image_from_json = data_from_json.get("image")
print(image_from_json[0][:50])

array_from_list = np.array(image_from_json, dtype="uint8")
print(array_from_list[0][:50])

new_image = Image.fromarray(array_from_list)
#new_image.show()

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel()

qt_image = ImageQt.ImageQt(new_image)
label.setPixmap(QPixmap.fromImage(qt_image).copy())

label.show()

image_from_pix = Image.fromqpixmap(label.pixmap())
image_from_pix.show()

app.exec_()
