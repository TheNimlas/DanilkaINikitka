# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_maps(object):
    def setupUi(self, maps):
        maps.setObjectName("maps")
        maps.resize(668, 555)
        self.map = QtWidgets.QLabel(maps)
        self.map.setGeometry(QtCore.QRect(10, 10, 641, 531))
        self.map.setText("")
        self.map.setObjectName("map")

        self.retranslateUi(maps)
        QtCore.QMetaObject.connectSlotsByName(maps)

    def retranslateUi(self, maps):
        _translate = QtCore.QCoreApplication.translate
        maps.setWindowTitle(_translate("maps", "nimals_and_danilus_maps"))
