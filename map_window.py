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
        self.map.setGeometry(QtCore.QRect(10, 0, 651, 481))
        self.map.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.map.setText("")
        self.map.setObjectName("map")
        self.verticalLayoutWidget = QtWidgets.QWidget(maps)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 20, 171, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ma_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.ma_format.setFont(font)
        self.ma_format.setStyleSheet("QPushButton{\n"
"            background-color: rgb(0, 0, 0);\n"
"            color: #fcfaff;\n"
"             border-radius: 17px transparent;\n"
"           border-bottom: 3px transparent;\n"
"            border-right: 2px transparent;\n"
"            border-left: 2px transparent;}\n"
"            QPushButton:hover{\n"
"            background-color: rgb(255,0,0);} \n"
"            QPushButton:pressed  {\n"
"            background-color: rgb(232,95,76); } ")
        self.ma_format.setObjectName("ma_format")
        self.verticalLayout.addWidget(self.ma_format)
        self.sat_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.sat_format.setFont(font)
        self.sat_format.setStyleSheet("QPushButton{\n"
"            background-color: rgb(0, 0, 0);\n"
"            color: #fcfaff;\n"
"             border-radius: 17px transparent;\n"
"           border-bottom: 3px transparent;\n"
"            border-right: 2px transparent;\n"
"            border-left: 2px transparent;}\n"
"            QPushButton:hover{\n"
"            background-color: rgb(255,0,0);} \n"
"            QPushButton:pressed  {\n"
"            background-color: rgb(232,95,76); } ")
        self.sat_format.setObjectName("sat_format")
        self.verticalLayout.addWidget(self.sat_format)
        self.gibrid_format = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.gibrid_format.setFont(font)
        self.gibrid_format.setStyleSheet("QPushButton{\n"
"            background-color: rgb(0, 0, 0);\n"
"            color: #fcfaff;\n"
"             border-radius: 17px transparent;\n"
"           border-bottom: 3px transparent;\n"
"            border-right: 2px transparent;\n"
"            border-left: 2px transparent;}\n"
"            QPushButton:hover{\n"
"            background-color: rgb(255,0,0);} \n"
"            QPushButton:pressed  {\n"
"            background-color: rgb(232,95,76); } ")
        self.gibrid_format.setObjectName("gibrid_format")
        self.verticalLayout.addWidget(self.gibrid_format)
        self.find_line = QtWidgets.QLineEdit(maps)
        self.find_line.setGeometry(QtCore.QRect(670, 420, 161, 41))
        self.find_line.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.find_line.setObjectName("find_line")
        self.find_button = QtWidgets.QPushButton(maps)
        self.find_button.setGeometry(QtCore.QRect(690, 472, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton{\n"
"            background-color: rgb(0, 0, 0);\n"
"            color: #fcfaff;\n"
"             border-radius: 17px transparent;\n"
"           border-bottom: 3px transparent;\n"
"            border-right: 2px transparent;\n"
"            border-left: 2px transparent;}\n"
"            QPushButton:hover{\n"
"            background-color: rgb(255,0,0);} \n"
"            QPushButton:pressed  {\n"
"            background-color: rgb(232,95,76); } ")
        self.find_button.setObjectName("find_button")
        self.verticalLayoutWidget.raise_()
        self.map.raise_()
        self.find_line.raise_()
        self.find_button.raise_()

        self.retranslateUi(maps)
        QtCore.QMetaObject.connectSlotsByName(maps)

    def retranslateUi(self, maps):
        _translate = QtCore.QCoreApplication.translate
        maps.setWindowTitle(_translate("maps", "nimals_and_danilus_maps"))
        self.ma_format.setText(_translate("maps", "Формат карты"))
        self.sat_format.setText(_translate("maps", "Формат спутника"))
        self.gibrid_format.setText(_translate("maps", "Hybrid"))
        self.find_button.setText(_translate("maps", "Find"))
