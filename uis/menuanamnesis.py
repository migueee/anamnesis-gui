# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuanamnesis.ui'
#
# Created: Mon Jan 19 13:28:40 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MenuAnamnesis(object):
    def setupUi(self, MenuAnamnesis):
        MenuAnamnesis.setObjectName(_fromUtf8("MenuAnamnesis"))
        MenuAnamnesis.resize(479, 181)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./img/aav.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuAnamnesis.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MenuAnamnesis)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 451, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 458, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runbusqueda = QtGui.QLineEdit(self.layoutWidget)
        self.runbusqueda.setObjectName(_fromUtf8("runbusqueda"))
        self.horizontalLayout.addWidget(self.runbusqueda)
        self.buscar = QtGui.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./img/buscar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buscar.setIcon(icon1)
        self.buscar.setObjectName(_fromUtf8("buscar"))
        self.horizontalLayout.addWidget(self.buscar)
        self.nuevo = QtGui.QPushButton(self.layoutWidget)
        self.nuevo.setObjectName(_fromUtf8("nuevo"))
        self.horizontalLayout.addWidget(self.nuevo)
        MenuAnamnesis.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MenuAnamnesis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MenuAnamnesis.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MenuAnamnesis)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MenuAnamnesis.setStatusBar(self.statusbar)

        self.retranslateUi(MenuAnamnesis)
        QtCore.QMetaObject.connectSlotsByName(MenuAnamnesis)

    def retranslateUi(self, MenuAnamnesis):
        MenuAnamnesis.setWindowTitle(_translate("MenuAnamnesis", "ANAMNESIS", None))
        self.label.setText(_translate("MenuAnamnesis", "Gestión de Anamnesis Vocal", None))
        self.label_2.setText(_translate("MenuAnamnesis", "Ingrese r.u.n. para buscar un paciente", None))
        self.buscar.setText(_translate("MenuAnamnesis", "Buscar", None))
        self.nuevo.setText(_translate("MenuAnamnesis", "Crear Nuevo", None))

