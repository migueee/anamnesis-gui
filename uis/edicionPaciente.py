# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edicionPaciente.ui'
#
# Created: Tue Feb 17 00:25:44 2015
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

class Ui_edicionPaciente(object):
    def setupUi(self, edicionPaciente):
        edicionPaciente.setObjectName(_fromUtf8("edicionPaciente"))
        edicionPaciente.resize(664, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./img/aav50.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edicionPaciente.setWindowIcon(icon)
        edicionPaciente.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(edicionPaciente)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 70, 661, 131))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.dpocupacion = QtGui.QLineEdit(self.frame)
        self.dpocupacion.setObjectName(_fromUtf8("dpocupacion"))
        self.gridLayout.addWidget(self.dpocupacion, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.dphuocupacion = QtGui.QSpinBox(self.frame)
        self.dphuocupacion.setMaximum(24)
        self.dphuocupacion.setObjectName(_fromUtf8("dphuocupacion"))
        self.gridLayout.addWidget(self.dphuocupacion, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.dpactextras = QtGui.QTextEdit(self.frame)
        self.dpactextras.setObjectName(_fromUtf8("dpactextras"))
        self.gridLayout.addWidget(self.dpactextras, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.dphuextra = QtGui.QSpinBox(self.frame)
        self.dphuextra.setMaximum(24)
        self.dphuextra.setObjectName(_fromUtf8("dphuextra"))
        self.gridLayout.addWidget(self.dphuextra, 1, 3, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(375, 0, 281, 64))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.dpfnacimiento = QtGui.QDateEdit(self.layoutWidget)
        self.dpfnacimiento.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dpfnacimiento.setObjectName(_fromUtf8("dpfnacimiento"))
        self.gridLayout_2.addWidget(self.dpfnacimiento, 1, 1, 1, 1)
        self.lrun = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lrun.setFont(font)
        self.lrun.setObjectName(_fromUtf8("lrun"))
        self.gridLayout_2.addWidget(self.lrun, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 220, 291, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.dparea = QtGui.QLineEdit(self.layoutWidget1)
        self.dparea.setMinimumSize(QtCore.QSize(40, 0))
        self.dparea.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dparea.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.dparea.setObjectName(_fromUtf8("dparea"))
        self.horizontalLayout_5.addWidget(self.dparea)
        self.dpfonocontacto = QtGui.QLineEdit(self.layoutWidget1)
        self.dpfonocontacto.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.dpfonocontacto.setObjectName(_fromUtf8("dpfonocontacto"))
        self.horizontalLayout_5.addWidget(self.dpfonocontacto)
        self.layoutWidget2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(310, 220, 341, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.layoutWidget2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.dpemail = QtGui.QLineEdit(self.layoutWidget2)
        self.dpemail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.dpemail.setObjectName(_fromUtf8("dpemail"))
        self.horizontalLayout_6.addWidget(self.dpemail)
        self.layoutWidget3 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 250, 641, 91))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_11 = QtGui.QLabel(self.layoutWidget3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.dpmotivo = QtGui.QTextEdit(self.layoutWidget3)
        self.dpmotivo.setObjectName(_fromUtf8("dpmotivo"))
        self.horizontalLayout_7.addWidget(self.dpmotivo)
        self.layoutWidget4 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 350, 298, 29))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.dpguardar = QtGui.QPushButton(self.layoutWidget4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./img/edit16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dpguardar.setIcon(icon1)
        self.dpguardar.setObjectName(_fromUtf8("dpguardar"))
        self.horizontalLayout_8.addWidget(self.dpguardar)
        self.layoutWidget5 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 0, 361, 66))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dpnombre = QtGui.QLineEdit(self.layoutWidget5)
        self.dpnombre.setObjectName(_fromUtf8("dpnombre"))
        self.horizontalLayout.addWidget(self.dpnombre)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.layoutWidget5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.dpapellido = QtGui.QLineEdit(self.layoutWidget5)
        self.dpapellido.setObjectName(_fromUtf8("dpapellido"))
        self.horizontalLayout_2.addWidget(self.dpapellido)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        edicionPaciente.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(edicionPaciente)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 664, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        edicionPaciente.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(edicionPaciente)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        edicionPaciente.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(edicionPaciente)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        edicionPaciente.setStatusBar(self.statusBar)

        self.retranslateUi(edicionPaciente)
        QtCore.QMetaObject.connectSlotsByName(edicionPaciente)

    def retranslateUi(self, edicionPaciente):
        edicionPaciente.setWindowTitle(_translate("edicionPaciente", "Agregar nuevo paciente", None))
        self.label_5.setText(_translate("edicionPaciente", "Ocupación", None))
        self.label_7.setText(_translate("edicionPaciente", "Horas uso \n"
"vocal continuo", None))
        self.label_4.setText(_translate("edicionPaciente", "Actividades Extra \n"
"que requieren un \n"
"uso vocal constante \n"
"o aumentado.", None))
        self.label_8.setText(_translate("edicionPaciente", "Horas uso \n"
"vocal continuo", None))
        self.label_2.setText(_translate("edicionPaciente", "R.U.N.", None))
        self.label_3.setText(_translate("edicionPaciente", "fecha nacimiento", None))
        self.dpfnacimiento.setDisplayFormat(_translate("edicionPaciente", "dd/MM/yyyy", None))
        self.lrun.setText(_translate("edicionPaciente", "lrun", None))
        self.label_9.setText(_translate("edicionPaciente", "Número Contacto", None))
        self.label_10.setText(_translate("edicionPaciente", "Correo Electrónico", None))
        self.label_11.setText(_translate("edicionPaciente", "Motivo Consulta", None))
        self.dpguardar.setText(_translate("edicionPaciente", "Actualizar", None))
        self.label.setText(_translate("edicionPaciente", "Nombres", None))
        self.label_6.setText(_translate("edicionPaciente", "Apellidos", None))
