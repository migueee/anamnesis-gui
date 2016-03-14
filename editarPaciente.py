# -*- encoding: utf-8 -*-
#a manopla
import sys
from PyQt4                   import QtCore, QtGui
from uis.edicionPaciente     import Ui_edicionPaciente
from bdd.datospersonalescrud import Cruddp

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

#TODO: falta recuperar la fecha el elemento QDateEdit
class UiEdicion(QtGui.QMainWindow):
	def __init__(self, run):
		QtGui.QMainWindow.__init__(self)
		self.ventana = Ui_edicionPaciente()
		self.ventana.setupUi(self)
		self.run = run
		self.paciente = Cruddp()
		self.datos = self.paciente.retornaPaciente(self.run)
		
		self.ventana.lrun.setText(str(self.run))
		self.ventana.dpnombre.setText(str(self.datos[0][2]))
		self.ventana.dpapellido.setText(str(self.datos[0][3]))
		#self.ventana.dpfnacimiento.dateTime(self.datos[0][4])
		self.ventana.dpocupacion.setText(str(self.datos[0][5]))
		self.ventana.dphuocupacion.setValue(int(self.datos[0][6]))
		self.ventana.dpactextras.setText(str(self.datos[0][7]))
		self.ventana.dphuextra.setValue(int(self.datos[0][8]))
		self.ventana.dparea.setText(str(self.datos[0][9]))
		self.ventana.dpfonocontacto.setText(str(self.datos[0][10]))
		self.ventana.dpemail.setText(str(self.datos[0][11]))
		self.ventana.dpmotivo.setText(str(self.datos[0][12]))
		
		self.connect(self.ventana.dpguardar, QtCore.SIGNAL('clicked()'), self.editar)

	def editar(self):
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
		dpp = (self.run, nom, apl, fnc, ocp, hoc, ext, exh, cod, fon, eml, mot)
		#print(dpp)
		guarda = Cruddp()
		guarda.actualizarPaciente(dpp)
		QtGui.QMessageBox.question(self, 'Alerta', _fromUtf8('Paciente actualizada correctamente.'))
		self.hide()
