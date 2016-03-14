# -*- encoding: utf-8 -*-
#a manopla
import sys
from PyQt4                    import QtCore, QtGui
from uis.datospersonalesnuevo import Ui_MainWindow
from bdd.datospersonalescrud  import Cruddp
from presentacionPaciente     import PresentarPaciente

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

class Paciente(QtGui.QMainWindow):
	def __init__(self):
        #print "inciando constructor"
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
		
		if(guarda.insertarPaciente(dpp)):
			QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('Paciente ingresado correctamente.'))
			self.ventana = PresentarPaciente(run)
			self.hide()
			self.ventana.show()
		else:
			QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('El run ingresado ya esta en la base de datos.'))
