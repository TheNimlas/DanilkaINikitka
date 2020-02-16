# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_maps(object):
    def setupUi(self, maps):
        maps.setObjectName("maps")
        maps.resize(863, 519)
        self.map = QtWidgets.QLabel(maps)
        self.map.setGeometry(QtCore.QRect(10, 10, 651, 481))
        self.map.setText("")
        self.map.setObjectName("map")
        self.ma_format = QtWidgets.QPushButton(maps)
        self.ma_format.setGeometry(QtCore.QRect(720, 40, 111, 31))
        self.ma_format.setObjectName("ma_format")
        self.sat_format = QtWidgets.QPushButton(maps)
        self.sat_format.setGeometry(QtCore.QRect(720, 80, 111, 31))
        self.sat_format.setObjectName("sat_format")
        self.gibrid_format = QtWidgets.QPushButton(maps)
        self.gibrid_format.setGeometry(QtCore.QRect(720, 120, 111, 31))
        self.gibrid_format.setObjectName("gibrid_format")

        self.retranslateUi(maps)
        QtCore.QMetaObject.connectSlotsByName(maps)

    def retranslateUi(self, maps):
        _translate = QtCore.QCoreApplication.translate
        maps.setWindowTitle(_translate("maps", "nimals_and_danilus_maps"))
        self.ma_format.setText(_translate("maps", "формат карты"))
        self.sat_format.setText(_translate("maps", "формат спутника"))
        self.gibrid_format.setText(_translate("maps", "гибридный формат"))

