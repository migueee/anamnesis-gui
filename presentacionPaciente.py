# -*- encoding: utf-8 -*-
#a manopla
import sys
from PyQt4                   import QtCore, QtGui
from uis.buscarpaciente      import Ui_MostrarPaciente
from bdd.datospersonalescrud import Cruddp
from bdd.sintomascrud        import CrudSyC
from bdd.evocalcrud          import CrudEV
from nuevoSintoma            import Sintomatologia
from nuevaEvaluacion         import Evaluacion
from presentacionEval        import PresentarEVocal
from presentacionSintoma     import PresentarSintomas
from editarPaciente          import UiEdicion

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

class PresentarPaciente(QtGui.QMainWindow):
	def __init__(self, run):
		QtGui.QMainWindow.__init__(self)
		self.ventanaPP = Ui_MostrarPaciente()
		self.ventanaPP.setupUi(self)
		self.run = run
		self.ventanaPS = Sintomatologia(self.run)
		self.ventanaPE = Evaluacion(self.run)
		
		#llenando tab 1
		#creamos un objeto de la bdd y buscamos el run
		self.busca = Cruddp()
		self.listaDatos = self.busca.retornaPaciente(run)
		#se cargan los datos en la pantalla con la información devuelta de la consulta
		self.ventanaPP.lRun.setText(str(self.listaDatos[0][1]))
		self.ventanaPP.lNombre.setText(str(self.listaDatos[0][2]))
		self.ventanaPP.lApellido.setText(str(self.listaDatos[0][3]))
		self.ventanaPP.lFecha.setText(str(self.listaDatos[0][4]))
		self.ventanaPP.lOcupacion.setText(str(self.listaDatos[0][5]))
		self.ventanaPP.lHOcupacion.setText(str(self.listaDatos[0][6]))
		self.ventanaPP.lActividades.setText(str(self.listaDatos[0][7]))
		self.ventanaPP.lHActividad.setText(str(self.listaDatos[0][8]))
		telefono = str(self.listaDatos[0][9])+"-"+str(self.listaDatos[0][10])
		self.ventanaPP.lFono.setText(str(telefono))
		self.ventanaPP.lEmail.setText(str(self.listaDatos[0][11]))
		self.ventanaPP.lMotivo.setText(str(self.listaDatos[0][12]))
		
		#llenando tab 2
		self.objetoSintomas   = CrudSyC()
		self.todoslosSintomas = self.objetoSintomas.retornaIdFecha(run)
		cont = 0
		for row in self.todoslosSintomas:
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeSintomas)
			aidi, fecha = row
			self.ventanaPP.treeSintomas.topLevelItem(cont).setText(0, str(aidi))
			self.ventanaPP.treeSintomas.topLevelItem(cont).setText(1, str(fecha))
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeSintomas)
			cont = cont + 1
		
		#llenado tab 3
		self.objetoEvaluaciones = CrudEV()
		self.todaslasEval       = self.objetoEvaluaciones.retornaIdFechaEV(run)
		cont = 0
		for row in self.todaslasEval:
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeEval)
			aidi, fecha = row
			self.ventanaPP.treeEval.topLevelItem(cont).setText(0, str(aidi))
			self.ventanaPP.treeEval.topLevelItem(cont).setText(1, str(fecha))
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeEval)
			cont = cont + 1
		
		#añadiendo las señales
		self.connect(self.ventanaPP.botonEditar, QtCore.SIGNAL('clicked()'), self.editarPersona)
		self.connect(self.ventanaPP.nuevoSintoma, QtCore.SIGNAL('clicked()'), self.nuevaSintomatologia)
		self.connect(self.ventanaPP.verSintoma, QtCore.SIGNAL('clicked()'), self.verSintoma)
		self.connect(self.ventanaPP.elimSintoma, QtCore.SIGNAL('clicked()'), self.eliminarSintoma)
		self.connect(self.ventanaPP.nuevaEval, QtCore.SIGNAL('clicked()'), self.nuevaEvocal)
		self.connect(self.ventanaPP.verEval, QtCore.SIGNAL('clicked()'), self.verEvocal)
		self.connect(self.ventanaPP.elimEval, QtCore.SIGNAL('clicked()'), self.eliminarEvocal)
		self.connect(self.ventanaPP.treeEval, QtCore.SIGNAL("itemPressed(QTreeWidgetItem*, int)"), self.seleccionE)
		self.connect(self.ventanaPP.treeSintomas, QtCore.SIGNAL("itemPressed(QTreeWidgetItem*, int)"), self.seleccionS)
		
	def seleccionS(self):
		self.seleccionado = self.ventanaPP.treeSintomas.currentItem()
		self.aidis = self.seleccionado.text(0)
		
	def seleccionE(self):
		self.seleccionado = self.ventanaPP.treeEval.currentItem()
		self.aidie = self.seleccionado.text(0)
	
	def llenarSintomas(self):
		self.todaslasEval = self.objetoEvaluaciones.retornaIdFechaEV(self.run)
		cont = 0
		self.ventanaPP.treeSintomas.reset()
		for row in self.todaslasEval:
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeSintomas)
			aidi, fecha = row
			self.ventanaPP.treeSintomas.topLevelItem(cont).setText(0, str(aidi))
			self.ventanaPP.treeSintomas.topLevelItem(cont).setText(1, str(fecha))
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeSintomas)
			print cont
			cont = cont + 1
		
	def llenarEvaluaciones(self):
		self.todaslasEval = self.objetoEvaluaciones.retornaIdFechaEV(self.run)
		cont = 0
		self.ventanaPP.treeEval.reset()
		for row in self.todaslasEval:
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeEval)
			aidi, fecha = row
			self.ventanaPP.treeEval.topLevelItem(cont).setText(0, str(aidi))
			self.ventanaPP.treeEval.topLevelItem(cont).setText(1, str(fecha))
			item_0 = QtGui.QTreeWidgetItem(self.ventanaPP.treeEval)
			print cont
			cont = cont + 1
		
	def editarPersona(self):
		self.ventanaPP = UiEdicion(self.run)
		self.ventanaPP.show()
		self.hide()
		
	def nuevaSintomatologia(self):
		self.ventanaPS = Sintomatologia(self.run)
		self.ventanaPS.show()
		self.llenarSintomas()
		
	def verSintoma(self):
		self.seleccionado = self.ventanaPP.treeSintomas.currentItem()
		#print self.seleccionado.text(0)
		self.aidis = self.seleccionado.text(0)
		self.ventanaPS = PresentarSintomas(self.run, self.aidis)
		self.ventanaPS.show()
		
	def eliminarSintoma(self):
		if self.aidis:
			respuestas = QtGui.QMessageBox.question(self,  'Consulta',  _fromUtf8('¿Seguro que desea eliminar la ficha de\nsintomalogía y conductas seleccionada?'),  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
			if respuestas == QtGui.QMessageBox.Yes:
				self.objetoSintomas.eliminarSintoma(self.aidis)
		else:
			QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('Debes seleccionar una sintomatología para eliminar.'))
		self.llenarSintomas()
		
	def nuevaEvocal(self):
		self.ventanaPE = Evaluacion(self.run)
		self.ventanaPE.show()
		self.llenarEvaluaciones()
		
	def verEvocal(self):
		self.seleccionado = self.ventanaPP.treeEval.currentItem()
		print self.seleccionado.text(0)
		self.aidie = self.seleccionado.text(0)
		self.ventanaPE = PresentarEVocal(self.run, self.aidie)
		self.ventanaPE.show()
	
	def eliminarEvocal(self):
		if self.aidie:
			respuestae = QtGui.QMessageBox.question(self,  'Consulta',  _fromUtf8('¿Seguro que desea eliminar la evaluación vocal seleccionada?'),  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
			if respuestae == QtGui.QMessageBox.Yes:
				self.objetoEvaluaciones.eliminarEvocal(self.aidis)
		else:
			QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('Selecciona una evaluación vocal para poder eliminar.'))
		self.llenarEvaluaciones()
