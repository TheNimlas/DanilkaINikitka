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
        maps.resize(863, 519)
        self.map = QtWidgets.QLabel(maps)
        self.map.setGeometry(QtCore.QRect(10, 10, 651, 481))
        self.map.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.map.setText("")
        self.map.setObjectName("map")
        self.verticalLayoutWidget = QtWidgets.QWidget(maps)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(690, 20, 160, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ma_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ma_format.setObjectName("ma_format")
        self.verticalLayout.addWidget(self.ma_format)
        self.sat_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sat_format.setObjectName("sat_format")
        self.verticalLayout.addWidget(self.sat_format)
        self.gibrid_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.gibrid_format.setObjectName("gibrid_format")
        self.verticalLayout.addWidget(self.gibrid_format)
        self.verticalLayoutWidget.raise_()
        self.map.raise_()

        self.retranslateUi(maps)
        QtCore.QMetaObject.connectSlotsByName(maps)

    def retranslateUi(self, maps):
        _translate = QtCore.QCoreApplication.translate
        maps.setWindowTitle(_translate("maps", "nimals_and_danilus_maps"))
        self.ma_format.setText(_translate("maps", "формат карты"))
        self.sat_format.setText(_translate("maps", "формат спутника"))
        self.gibrid_format.setText(_translate("maps", "гибридный формат"))
