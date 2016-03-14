# -*- encoding: utf-8 -*-
#a manopla
import sys
from PyQt4 import QtCore, QtGui
from uis.datospersonalesnuevo import Ui_MainWindow
from bdd.datospersonalescrud import Cruddp

class Paciente(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ventana = Ui_MainWindow()
		self.ventana.setupUi(self)
		self.connect(self.ventana.dpguardar, QtCore.SIGNAL('clicked()'), self.guardar)

	def guardar(self):
		#dpp = 0
		nom = str(self.ventana.dpnombre.text())
		apl = str(self.ventana.dpapellido.text())
		fnc = str(self.ventana.dpfnacimiento.text())
		ocp = str(self.ventana.dpocupacion.text())
		hoc = int(self.ventana.dphuocupacion.text())
		ext = str(self.ventana.dpactextras.toPlainText())
		exh = int(self.ventana.dphuextra.text())
		cod = int(self.ventana.dparea.text())
		fon = int(self.ventana.dpfonocontacto.text())
		eml = str(self.ventana.dpemail.text())
		mot = str(self.ventana.dpmotivo.toPlainText())
		run = str(self.ventana.lineEdit.text())
		dpp = (run, nom, apl, fnc, ocp, hoc, ext, exh, cod, fon, eml, mot)
		#print(dpp)
		guarda = Cruddp()
		guarda.insertarPaciente(dpp)

def main():
	app = QtGui.QApplication(sys.argv)
	ventana = Paciente()
	ventana.show()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()

