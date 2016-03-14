# -*- encoding: utf-8 -*-
import sys
from PyQt4                   import QtCore, QtGui
from uis.consultaevocal      import Ui_vistaEvocal
from bdd.datospersonalescrud import Cruddp
from bdd.evocalcrud          import CrudEV

class PresentarEVocal(QtGui.QMainWindow):
	def __init__(self, run, aidi):
		print "presentando Evaluación Vocal."
		QtGui.QMainWindow.__init__(self)
		self.ventanaPE = Ui_vistaEvocal()
		self.ventanaPE.setupUi(self)
		self.run  = run
		self.aidi = aidi
		
		self.paciente   = Cruddp()
		self.nombreP    = self.paciente.retornaNombre(run)
		
		self.evaluacion = CrudEV()
		
		self.ventanaPE.labelNombre.setText(self.nombreP)
		self.ventanaPE.labelRun.setText(str(run))
		
		#cargar toda la información en la UI
		
		#tab 1
		self.todaEval   = self.evaluacion.retornaEvalVocal(self.aidi)
		self.ventanaPE.labelFecha.setText(str(self.todaEval[0][2]))
		
		self.ventanaPE.lcdVHIFun.display(int(self.todaEval[0][3]))
		self.ventanaPE.lcdVHIFis.display(int(self.todaEval[0][4]))
		self.ventanaPE.lcdVHIEmo.display(int(self.todaEval[0][5]))
		self.ventanaPE.lcdVHITotal.display(int(self.todaEval[0][6]))
		
		self.ventanaPE.labeltrr.setText(self.recuperarTipoRespiratorio(self.todaEval[0][7]))
		self.ventanaPE.label_53.setText(self.recuperarTipoRespiratorio(self.todaEval[0][8]))
		self.ventanaPE.labelmrr.setText(self.recuperarModoRespiratorio(self.todaEval[0][9]))
		self.ventanaPE.labelmrf.setText(self.recuperarModoRespiratorio(self.todaEval[0][10]))
		self.ventanaPE.labelcrf.setText(self.recuperarCoordFR(self.todaEval[0][11]))
		self.ventanaPE.lcdnidc.display(int(self.todaEval[0][12]))
		self.ventanaPE.lcdtmf.display(int(self.todaEval[0][13]))
		self.ventanaPE.lcdtme.display(int(self.todaEval[0][14]))
		self.ventanaPE.lcdisa.display(str(float(self.todaEval[0][15])))
		self.ventanaPE.labelar.setText(self.recuperarApoyo(self.todaEval[0][16]))
		
		#tab 2
		self.ventanaPE.labelppf1.setText(self.recuperarPlano(self.todaEval[0][17]))
		self.ventanaPE.labelppf2.setText(self.recuperarPlano(self.todaEval[0][18]))
		self.ventanaPE.labelppf3.setText(self.recuperarPlano(self.todaEval[0][19]))
		self.ventanaPE.labelppl1.setText(self.recuperarPlanoLateral(self.todaEval[0][20]))
		self.ventanaPE.labelppl2.setText(self.recuperarPlanoLateral(self.todaEval[0][21]))
		self.ventanaPE.labelppl3.setText(self.recuperarPlanoLateral(self.todaEval[0][22]))
		self.ventanaPE.labelppp1.setText(self.recuperarPlano(self.todaEval[0][23]))
		self.ventanaPE.labelppp2.setText(self.recuperarPlano(self.todaEval[0][24]))
		self.ventanaPE.labelppp3.setText(self.recuperarPlano(self.todaEval[0][25]))
		self.ventanaPE.obspt.setText(str(self.todaEval[0][26]))

		self.ventanaPE.labeltg.setText(self.recuperarTonicidad(self.todaEval[0][27]))
		self.ventanaPE.labelti.setText(self.recuperarTonicidad(self.todaEval[0][28]))
		self.ventanaPE.labelts.setText(self.recuperarTonicidad(self.todaEval[0][29]))
		self.ventanaPE.labeltc.setText(self.recuperarTonicidad(self.todaEval[0][30]))
		self.ventanaPE.labeltce.setText(self.recuperarTonicidad(self.todaEval[0][31]))
		self.ventanaPE.labeltal.setText(self.recuperarTonicidadAL(self.todaEval[0][32]))
		
		#tab 3
		self.ventanaPE.lcdhpa.display(int(self.todaEval[0][33]))
		self.ventanaPE.lcdhec.display(int(self.todaEval[0][34]))
		self.ventanaPE.lcdhpp.display(int(self.todaEval[0][35]))
		self.ventanaPE.lcdhde.display(int(self.todaEval[0][36]))
		self.ventanaPE.lcdhrh.display(int(self.todaEval[0][37]))
		self.ventanaPE.lcdhpt.display(int(self.todaEval[0][38]))
		
		self.ventanaPE.labelrr.setText(self.recuperarRasati(self.todaEval[0][39]))
		self.ventanaPE.labelra.setText(self.recuperarRasati(self.todaEval[0][40]))
		self.ventanaPE.labelrs.setText(self.recuperarRasati(self.todaEval[0][41]))
		self.ventanaPE.labelras.setText(self.recuperarRasati(self.todaEval[0][42]))
		self.ventanaPE.labelrt.setText(self.recuperarRasati(self.todaEval[0][43]))
		self.ventanaPE.labelri.setText(self.recuperarRasati(self.todaEval[0][44]))
		
		self.ventanaPE.lcdtmh.display(int(self.todaEval[0][45]))
		
		#tab 4
		self.ventanaPE.lcdj.display(str(float(self.todaEval[0][46])))
		self.ventanaPE.lcds.display(str(float(self.todaEval[0][47])))
		self.ventanaPE.lcdnhr.display(int(self.todaEval[0][48]))
		
		self.ventanaPE.lcdff.display(int(self.todaEval[0][49]))
		self.ventanaPE.lcdrf.display(int(self.todaEval[0][50]))
		self.ventanaPE.lcdrtet.display(int(self.todaEval[0][51]))
		self.ventanaPE.lcdt.display(int(self.todaEval[0][52]))
		
		self.ventanaPE.labeltipo.setText(self.recuperarTipoCantante(self.todaEval[0][53]))
		self.ventanaPE.labelcbh.setText(self.recuperarClasificacionVocalHombre(self.todaEval[0][54]))
		self.ventanaPE.labelcbm.setText(self.recuperarClasificacionVocalMujer(self.todaEval[0][55]))
		
	def recuperarTipoRespiratorio(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Costal alto"
		elif n == 2:
			return "Abdominal"
		elif n == 3:
			return "Mixto"
		return u"Costo diafragmático"
		
	def recuperarModoRespiratorio(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Predomonio nasal"
		return "Predomonio bucal"

	def recuperarCoordFR(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Adecuada"
		elif n == 2:
			return "Regular"
		return "Pobre - alterada"
		
	def recuperarApoyo(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Bueno"
		elif n == 2:
			return "Regular"
		return "Malo"

	def recuperarPlano(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Adecuado"
		elif n == 2:
			return "Hacia derecha"
		return "Hacia izquierda"
		
	def recuperarPlanoLateral(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Adecuado"
		elif n == 2:
			return "Cabeza adelantada"
		elif n == 3:
			return "Hipercifosis"
		elif n == 4:
			return "Hiperlordosis"
		elif n == 5:
			return u"Rectificación cervical"
		elif n == 6:
			return "Rectificación dorsal"
		return u"Rectificación lumbar"
		
	def recuperarTonicidad(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return u"Eutonía"
		elif n == 2:
			return u"Hipotonía"
		return u"Hipertornía"
			
	def recuperarTonicidadAL(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Normal"
		elif n == 2:
			return "Ascendida"
		elif n == 3:
			return "Descendida"
		elif n == 4:
			return "Anteriorizada"
		elif n == 5:
			return "Posteriorizada"
		elif n == 6:
			return "Sin cracea"
		elif n == 7:
			return "Desplacamiento lateral hacia derecha"
		return "Desplacamiento lateral hacia izquierda"
	
	def recuperarRasati(self, n):
		if n == 0:
			return "Normal"
		elif n == 1:
			return "Leve"
		elif n == 2:
			return "Moderado"
		return "Intenso"
		
	def recuperarTipoCantante(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Cantante Popular"
		return u"Cantante Lírico"
	
	def recuperarClasificacionVocalHombre(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Tenor"
		elif n == 2:
			return u"Barítono"
		return "Bajo"
		
	def recuperarClasificacionVocalMujer(self, n):
		if n == 0:
			return "Ninguno"
		elif n == 1:
			return "Soprano"
		elif n == 2:
			return "Mezzosoprano"
		return "Contralto"
