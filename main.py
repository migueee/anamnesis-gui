# -*- encoding: utf-8 -*-
#archivo con pantalla inicial
import sys
import os
from PyQt4                   import QtCore, QtGui
from PyQt4                   import QtCore, QtGui
from uis.menuanamnesis       import Ui_MenuAnamnesis
from bdd.datospersonalescrud import Cruddp
from nuevoPaciente           import Paciente
from presentacionPaciente    import PresentarPaciente

class MainAnamnesis(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ventana = Ui_MenuAnamnesis()
		self.ventana.setupUi(self)
		self.connect(self.ventana.buscar, QtCore.SIGNAL('clicked()'), self.buscar)
		self.connect(self.ventana.nuevo, QtCore.SIGNAL('clicked()'), self.nuevo)
		
	def buscar(self):
		var = str(self.ventana.runbusqueda.text())
		run = var.encode('utf-8')
		busca = Cruddp()
		encontrado = busca.consultarRun(run)
		if encontrado == True:
			texto = "RUN ENCONTRADO"
			texto = texto.encode('utf-8')
			self.ventana.label_2.setText(str(texto))
			self.ventana = PresentarPaciente(run)
			self.ventana.show()
			self.hide()
		else:
			texto = "RUN ingresado NO se encuentra en la base de datos o NO es valido"
			texto = texto.encode('utf-8')
			self.ventana.label_2.setText(str(texto))
			
	def nuevo(self):
		self.ventana = Paciente()
		self.ventana.show()
		self.hide()

			
def main():
	app = QtGui.QApplication(sys.argv)
	ventana = MainAnamnesis()
	ventana.show()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()
