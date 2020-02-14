import sys
import requests
from PyQt5.QtGui import QPixmap
from map_window import Ui_maps
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget, Ui_maps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        map_request = "https://static-maps.yandex.ru/1.x/?ll=133.795384,-25.694768&spn=20.700,20.700&l=sat"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.jpg"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.map_pic = QPixmap(map_file)
        self.map.setPixmap(self.map_pic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
