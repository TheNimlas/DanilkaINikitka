import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from map_window import Ui_maps
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget, Ui_maps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_request = "https://static-maps.yandex.ru/1.x/?ll={},{}&" \
                           "spn={},{}&l={}"
        self.first_coord = 37.617635
        self.second_coord = 55.755814
        self.i = 0.005
        self.format = 'jpg'
        self.style = 'sat'
        self.response = requests.get(
            self.map_request.format(self.first_coord, self.second_coord, self.i, self.i,
                                    self.style))

        if not self.response:
            print("Ошибка выполнения запроса:")
            print(self.map_request)
            print("Http статус:", self.response.status_code, "(", self.response.reason, ")")
            sys.exit(1)
        map_file = "map.jpg"
        with open(map_file, "wb") as file:
            file.write(self.response.content)
        self.map_pic = QPixmap(map_file)
        self.map.setPixmap(self.map_pic)
        self.sat_format.clicked.connect(self.change_format)
        self.ma_format.clicked.connect(self.change_format)
        self.gibrid_format.clicked.connect(self.change_format)

    def place_a_map(self):
        map_file = "map.jpg"
        self.response = requests.get(
            self.map_request.format(self.first_coord, self.second_coord, self.i, self.i,
                                    self.style))
        if self.format == 'jpg':
            map_file = "map.jpg"
        elif self.format == 'png':
            map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(self.response.content)
        self.map_pic = QPixmap(map_file)
        self.map.setPixmap(self.map_pic)

    def change_format(self):
        if self.sender() == self.sat_format:
            self.format = 'jpg'
            self.style = 'sat'
        elif self.sender() == self.ma_format:
            self.format = 'png'
            self.style = 'map'
        elif self.sender() == self.gibrid_format:
            self.format = 'png'
            self.style = 'skl'
        self.place_a_map()

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            if self.i > 0:
                self.i -= 0.005
                self.place_a_map()
        elif event.key() == 16777239:
            if 0 <= self.i < 75:
                self.i += 0.005
                self.place_a_map()
        elif event.key() == QtCore.Qt.Key_Up:
            if self.second_coord < 55.756814:
                self.second_coord += 0.0002
                self.place_a_map()
        elif event.key() == QtCore.Qt.Key_Down:
            if self.second_coord > 55.754814:
                self.second_coord -= 0.0002
                self.place_a_map()
        elif event.key() == QtCore.Qt.Key_Right:
            if self.first_coord < 37.619635:
                self.first_coord += 0.0002
                self.place_a_map()
        elif event.key() == QtCore.Qt.Key_Left:
            if self.first_coord > 37.615635:
                self.first_coord -= 0.0002
                self.place_a_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
