# -*- encoding: utf-8 -*-
import sys
from PyQt4                      import QtCore, QtGui
from uis.consultaSintomatologia import Ui_consultaSintoma
from bdd.datospersonalescrud    import Cruddp
from bdd.sintomascrud           import CrudSyC

class PresentarSintomas(QtGui.QMainWindow):
	def __init__(self, run, aidi):
		print "presentando Evaluación Vocal."
		QtGui.QMainWindow.__init__(self)
		self.ventanaPS = Ui_consultaSintoma()
		self.ventanaPS.setupUi(self)
		self.run  = run
		self.aidi = aidi
		
		self.paciente = Cruddp()
		self.nombreP  = self.paciente.retornaNombre(run)
		
		self.sintoma  = CrudSyC()
		
		self.ventanaPS.nombrep.setText(self.nombreP)
		#por un error con la Ui el label que carga el run quedó con nombre 'apellidop', pero en realidad es el run
		self.ventanaPS.apellidop.setText(str(run))
		
		#cargar toda la información en la UI
		
		self.todaSintoma   = self.sintoma.retornaSintomatologia(self.aidi)
		self.ventanaPS.lfecha.setText(str(self.todaSintoma[0][2]))
		
		self.ventanaPS.lsv1.setText(self.recuperaSintoma(self.todaSintoma[0][3]))
		self.ventanaPS.dsv1.setText(str(self.todaSintoma[0][4]))
		self.ventanaPS.lsv2.setText(self.recuperaSintoma(self.todaSintoma[0][5]))
		self.ventanaPS.dsv2.setText(str(self.todaSintoma[0][6]))
		self.ventanaPS.lsv3.setText(self.recuperaSintoma(self.todaSintoma[0][7]))
		self.ventanaPS.dsv3.setText(str(self.todaSintoma[0][8]))
		self.ventanaPS.lsv4.setText(self.recuperaSintoma(self.todaSintoma[0][9]))
		self.ventanaPS.dsv4.setText(str(self.todaSintoma[0][10]))
		
		self.ventanaPS.los1.setText(self.recuperaOtroSintoma(self.todaSintoma[0][11]))
		self.ventanaPS.dos1.setText(str(self.todaSintoma[0][12]))
		self.ventanaPS.los2.setText(self.recuperaOtroSintoma(self.todaSintoma[0][13]))
		self.ventanaPS.dos2.setText(str(self.todaSintoma[0][14]))
		self.ventanaPS.los3.setText(self.recuperaOtroSintoma(self.todaSintoma[0][15]))
		self.ventanaPS.dos3.setText(str(self.todaSintoma[0][16]))
		self.ventanaPS.los4.setText(self.recuperaOtroSintoma(self.todaSintoma[0][17]))
		self.ventanaPS.dos4.setText(str(self.todaSintoma[0][18]))
		
		self.ventanaPS.tamg.setText(str(self.todaSintoma[0][19]))
		self.ventanaPS.tmqc.setText(str(self.todaSintoma[0][20]))
		
		self.ventanaPS.lcav1.setText(self.recuperaConducta(self.todaSintoma[0][21]))
		self.ventanaPS.dcav1.setText(str(self.todaSintoma[0][22]))
		self.ventanaPS.lcav2.setText(self.recuperaConducta(self.todaSintoma[0][23]))
		self.ventanaPS.dcav2.setText(str(self.todaSintoma[0][24]))
		self.ventanaPS.lcav3.setText(self.recuperaConducta(self.todaSintoma[0][25]))
		self.ventanaPS.dcav3.setText(str(self.todaSintoma[0][26]))
		self.ventanaPS.lcav4.setText(self.recuperaConducta(self.todaSintoma[0][27]))
		self.ventanaPS.dcav4.setText(str(self.todaSintoma[0][28]))
		
		self.ventanaPS.lcdhqd.display(int(self.todaSintoma[0][29]))
		
	def recuperaSintoma(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Ronquera"
		elif n == 2:
			return "Dolor fonar"
		elif n == 3:
			return "Fatiga"
		elif n == 4:
			return u"Sensación de cuerpo\nextraño"
		elif n == 5:
			return "Picor al hablar"
		elif n == 6:
			return "Carraspera"
		elif n == 7:
			return u"Tensión al hablar"
		elif n == 8:
			return "Resequedad"
		return u"Esfuerzo al hablar"
	
	def recuperaOtroSintoma(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return u"Problemas de acusión"
		elif n == 2:
			return u"Alergías"
		elif n == 3:
			return u"Resfríos frecuentes"
		elif n == 4:
			return u"Estrés"
		elif n == 5:
			return u"Acidez gástrica"
		elif n == 6:
			return u"Dificultad al tragar"
		elif n == 7:
			return "Dolor de cuello\nu hombros"
		return u"Pérdidas anteriores de\nla voz"
		
	def recuperaConducta(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Fumador"
		elif n == 2:
			return "Bebe Alcohol"
		elif n == 3:
			return "Consumo de alimentos\ncondimentados"
		elif n == 4:
			return "Consumo de liquidos"
		elif n == 5:
			return u"Consumo de café"
		elif n == 6:
			return "Pastillas de menta"
		elif n == 7:
			return "Intensidad vocal elevada"
		elif n == 8:
			return u"Realiza actividad física"
		elif n == 9:
			return "Se expone a cambios de\ntemperatura"
		return u"Se expone a calefacción"
