# -*- encoding: utf-8 -*-
#a manopla
import sys
import time
from PyQt4                   import QtCore, QtGui
from uis.sintomatologianuevo import Ui_SintomaConducta
from bdd.sintomascrud        import CrudSyC
from bdd.datospersonalescrud import Cruddp

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

class Sintomatologia(QtGui.QMainWindow):
	def __init__(self, run):
		QtGui.QMainWindow.__init__(self)
		self.run = run
		self.ventana = Ui_SintomaConducta()
		self.ventana.setupUi(self)
		
		self.paciente = Cruddp()
		self.nombreP = self.paciente.retornaNombre(run)
				
		self.ventana.nombrep.setText(self.nombreP)
		self.ventana.apellidop.setText(str(run))
		self.connect(self.ventana.bguardar, QtCore.SIGNAL('clicked()'), self.guardar)

	def guardar(self):
		#dpp = 0
		run   = self.run
		fecha = time.strftime("%d/%m/%Y")
		sv1   = int(self.ventana.svr1.currentIndex())
		dsv1  = str(self.ventana.dsvr1.text())
		sv2   = int(self.ventana.svr2.currentIndex())
		dsv2  = str(self.ventana.dsvr2.text())
		sv3   = int(self.ventana.svr3.currentIndex())
		dsv3  = str(self.ventana.dsvr3.text())
		sv4   = int(self.ventana.svr4.currentIndex())
		dsv4  = str(self.ventana.dsvr4.text())
		os1   = int(self.ventana.os1.currentIndex())
		dos1  = str(self.ventana.dos1.text())
		os2   = int(self.ventana.os2.currentIndex())
		dos2  = str(self.ventana.dos2.text())
		os3   = int(self.ventana.os3.currentIndex())
		dos3  = str(self.ventana.dos3.text())
		os4   = int(self.ventana.os4.currentIndex())
		dos4  = str(self.ventana.dos4.text())
		antm  = str(self.ventana.textAMG.toPlainText())
		med   = str(self.ventana.textMQC.toPlainText())
		cav1  = int(self.ventana.cav1.currentIndex())
		dcav1 = str(self.ventana.dcav1.text())
		cav2  = int(self.ventana.cav2.currentIndex())
		dcav2 = str(self.ventana.dcav2.text())
		cav3  = int(self.ventana.cav3.currentIndex())
		dcav3 = str(self.ventana.dcav3.text())
		cav4  = int(self.ventana.cav4.currentIndex())
		dcav4 = str(self.ventana.dcav4.text())
		hhd   = int(self.ventana.hqd.text())
		syc = (run, fecha, sv1, dsv1, sv2, dsv2, sv3, dsv3, sv4, dsv4, os1, dos1, os2, dos2, os3, dos3, os4, dos4, antm, med, cav1, dcav1, cav2, dcav2, cav3, dcav3, cav4, dcav4, hhd)
		#print(dpp)
		guarda = CrudSyC()
		guarda.insertarSintomatologia(syc)
		QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('Sintomatología agregada exitosamente.'))
		self.hide()
