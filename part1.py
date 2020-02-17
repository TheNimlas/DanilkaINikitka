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
                           "spn={},{}&l={}"  # &pt=37.617635,55.755814
        self.first_coord = 37.617635
        self.second_coord = 55.755814
        self.i = 0.005
        self.format = 'jpg'
        self.style = 'sat'
        self.params = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
                       'first_coord': self.first_coord,
                       'second_coord': self.second_coord,
                       'pt[0]': self.first_coord,
                       'pt[1]': self.second_coord}
        self.find_button.setText(chr(128269))
        self.ma_format.setText(chr(128506))
        self.sat_format.setText(chr(128752))
        self.response = requests.get(
            self.map_request.format(self.first_coord, self.second_coord, self.i, self.i,
                                    self.style))
        self.make_a_mark = False
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
        self.map.setFocus()
        self.sat_format.clicked.connect(self.change_format)
        self.ma_format.clicked.connect(self.change_format)
        self.gibrid_format.clicked.connect(self.change_format)
        self.find_button.clicked.connect(self.find)
        self.drop_button.clicked.connect(self.drop_result)

    def drop_result(self):
        self.map_request = "https://static-maps.yandex.ru/1.x/?ll={},{}&" \
                           "spn={},{}&l={}"
        self.make_a_mark = False
        self.place_a_map()

    def find(self):
        address = self.find_line.text()
        try:
            self.make_a_mark = True
            geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-" \
                               "98ba-98533de7710b&geocode={}&format=json".format(address)
            response = requests.get(geocoder_request)
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                "GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            self.params['first_coord'] = float(toponym_coodrinates.split()[0])
            self.params['second_coord'] = float(toponym_coodrinates.split()[1])
            self.first_coord = float(toponym_coodrinates.split()[0])
            self.second_coord = float(toponym_coodrinates.split()[1])
            self.params['pt[0]'] = float(toponym_coodrinates.split()[0])
            self.params['pt[1]'] = float(toponym_coodrinates.split()[1])
            self.place_a_map()
        except Exception as e:
            print(e.__class__.__name__)
            self.map_pic = QPixmap('error.jpg')
            self.map.setPixmap(self.map_pic)
            self.map.setFocus()

    def place_a_map(self):
        map_file = "map.jpg"
        if self.make_a_mark:
            self.map_request = "https://static-maps.yandex.ru/1.x/?ll={},{}&" \
                               "spn={},{}&l={}&pt={},{}"
            self.response = requests.get(
                self.map_request.format(self.params['first_coord'], self.params['second_coord'],
                                        self.i, self.i, self.style,
                                        self.params['pt[0]'], self.params['pt[1]']))
        else:
            self.response = requests.get(
                self.map_request.format(self.params['first_coord'], self.params['second_coord'],
                                        self.i, self.i, self.style))
        if self.format == 'jpg':
            map_file = "map.jpg"
        elif self.format == 'png':
            map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(self.response.content)
        self.map_pic = QPixmap(map_file)
        self.map.setPixmap(self.map_pic)
        self.map.setFocus()

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
        try:
            if event.key() == 16777238:
                if self.i > 0.005:
                    self.i -= 0.005
                    self.place_a_map()
            elif event.key() == 16777239:
                if 0 <= self.i < 75:
                    self.i += 0.005
                    self.place_a_map()
            elif event.key() == QtCore.Qt.Key_Up:
                if self.params['second_coord'] < 84:
                    self.params['second_coord'] += self.i
                    self.place_a_map()
            elif event.key() == QtCore.Qt.Key_Down:
                if self.params['second_coord'] > -84:
                    self.params['second_coord'] -= self.i
                    self.place_a_map()
            elif event.key() == QtCore.Qt.Key_Right:
                if self.params['first_coord'] < 179:
                    self.params['first_coord'] += 3 * self.i
                    self.place_a_map()
            elif event.key() == QtCore.Qt.Key_Left:
                if self.params['first_coord'] > -179:
                    self.params['first_coord'] -= 3 * self.i
                    self.place_a_map()
        except Exception as e:
            print(e.__class__.__name__)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
