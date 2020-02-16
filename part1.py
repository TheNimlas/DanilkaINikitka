import sys
import requests
from PyQt5.QtGui import QPixmap
from map_window import Ui_maps
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget, Ui_maps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_request = "https://static-maps.yandex.ru/1.x/?ll=37.617635,55.755814&" \
                           "spn={},{}&l=sat"
        self.i = 0.005
        self.response = requests.get(self.map_request.format(self.i, self.i))

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

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            if self.i - 0.005 > 0:
                self.i -= 0.005
                self.response = requests.get(self.map_request.format(self.i, self.i))
                map_file = "map.jpg"
                with open(map_file, "wb") as file:
                    file.write(self.response.content)
                self.map_pic = QPixmap(map_file)
                self.map.setPixmap(self.map_pic)
        elif event.key() == 16777239:
            if 0 <= self.i < 75:
                self.i += 0.005
                self.response = requests.get(self.map_request.format(self.i, self.i))
                map_file = "map.jpg"
                with open(map_file, "wb") as file:
                    file.write(self.response.content)
                self.map_pic = QPixmap(map_file)
                self.map.setPixmap(self.map_pic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


