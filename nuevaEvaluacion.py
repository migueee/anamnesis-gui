# -*- encoding: utf-8 -*-
import sys
import time
from PyQt4                   import QtCore, QtGui
from uis.evaluacionvocal     import Ui_EvaluacionVocal
from bdd.evocalcrud          import CrudEV
from bdd.datospersonalescrud import Cruddp

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

class Evaluacion(QtGui.QMainWindow):
	def __init__(self, run):
		QtGui.QMainWindow.__init__(self)
		self.run = run
		self.ventanaEV = Ui_EvaluacionVocal()
		self.ventanaEV.setupUi(self)

		self.paciente = Cruddp()
		self.nombreP = self.paciente.retornaNombre(run)

		self.ventanaEV.labelNombre.setText(self.nombreP)
		self.ventanaEV.labelRun.setText(str(run))

		#self.ventanaEV.lcdTotal.display(25)

		self.connect(self.ventanaEV.pushButton, QtCore.SIGNAL('clicked()'), self.guardar)

		#spin VHI
		#self.connect(self.ventanaEV.spinFuncional, QtCore.SIGNAL('valueChanged(int)'), self.ventanaEV.lcdTotal, QtCore.SLOT('display(calcularVHI())'))
		self.connect(self.ventanaEV.spinFuncional, QtCore.SIGNAL('editingFinished()'), self.calcularVHI)
		self.connect(self.ventanaEV.spinFisica, QtCore.SIGNAL('editingFinished()'), self.calcularVHI)
		self.connect(self.ventanaEV.spinEmocional, QtCore.SIGNAL('editingFinished()'), self.calcularVHI)

		#spin Indice S/A
		self.connect(self.ventanaEV.spinTMF, QtCore.SIGNAL('editingFinished()'), self.calcularISA)
		self.connect(self.ventanaEV.spinTME, QtCore.SIGNAL('editingFinished()'), self.calcularISA)

		#spin Hiperlaxitud
		self.connect(self.ventanaEV.spinHPHA, QtCore.SIGNAL('editingFinished()'), self.calcularPTH)
		self.connect(self.ventanaEV.spinHEC, QtCore.SIGNAL('editingFinished()'), self.calcularPTH)
		self.connect(self.ventanaEV.spinHPP, QtCore.SIGNAL('editingFinished()'), self.calcularPTH)
		self.connect(self.ventanaEV.spinHDE, QtCore.SIGNAL('editingFinished()'), self.calcularPTH)
		self.connect(self.ventanaEV.spinHRH, QtCore.SIGNAL('editingFinished()'), self.calcularPTH)


	def guardar(self):
		"""guarda mas datos que la ctm"""
		run    = self.run
		fecha  = time.strftime("%d/%m/%Y")
		vhifun = int(self.ventanaEV.spinFuncional.text())
		vhifis = int(self.ventanaEV.spinFisica.text())
		vhiemo = int(self.ventanaEV.spinEmocional.text())
		vhitot = int(self.ventanaEV.lcdTotal.intValue())
		trr    = int(self.ventanaEV.comboTRR.currentIndex())
		trf    = int(self.ventanaEV.comboTRF.currentIndex())
		mrr    = int(self.ventanaEV.comboMRR.currentIndex())
		mrf    = int(self.ventanaEV.comboBox_2.currentIndex())
		cfr    = int(self.ventanaEV.comboCFR.currentIndex())
		ni     = int(self.ventanaEV.spinNIDC.text())
		tmf    = int(self.ventanaEV.spinTMF.text())
		tme    = int(self.ventanaEV.spinTME.text())
		isa    = float(self.ventanaEV.lcdNumber.value())
		ar     = int(self.ventanaEV.comboAR.currentIndex())
		ppf1   = int(self.ventanaEV.cPPF1.currentIndex())
		ppf2   = int(self.ventanaEV.cPPF2.currentIndex())
		ppf3   = int(self.ventanaEV.cPPF3.currentIndex())
		ppl1   = int(self.ventanaEV.cPPL1.currentIndex())
		ppl2   = int(self.ventanaEV.cPPL2.currentIndex())
		ppl3   = int(self.ventanaEV.cPPL3.currentIndex())
		ppp1   = int(self.ventanaEV.cPPP1.currentIndex())
		ppp2   = int(self.ventanaEV.cPPP2.currentIndex())
		ppp3   = int(self.ventanaEV.cPPP3.currentIndex())
		po     = str(self.ventanaEV.observacionesPyT.toPlainText())
		tg     = int(self.ventanaEV.cTonG.currentIndex())
		ti     = int(self.ventanaEV.cTonI.currentIndex())
		ts     = int(self.ventanaEV.cTonS.currentIndex())
		te     = int(self.ventanaEV.cTonC.currentIndex())
		tce    = int(self.ventanaEV.cTonCE.currentIndex())
		ta     = int(self.ventanaEV.cTonAL.currentIndex())
		hpha   = int(self.ventanaEV.spinHPHA.text())
		hec    = int(self.ventanaEV.spinHEC.text())
		hpp    = int(self.ventanaEV.spinHPP.text())
		hde    = int(self.ventanaEV.spinHDE.text())
		hrh    = int(self.ventanaEV.spinHRH.text())
		hpt    = int(self.ventanaEV.lcdHPT.intValue())
		rr     = int(self.ventanaEV.comboRR.currentIndex())
		ra     = int(self.ventanaEV.comboRA.currentIndex())
		rs     = int(self.ventanaEV.comboRS.currentIndex())
		ras    = int(self.ventanaEV.comboRAst.currentIndex())
		rt     = int(self.ventanaEV.comboRT.currentIndex())
		ri     = int(self.ventanaEV.comboRI.currentIndex())
		tmh    = int(self.ventanaEV.spinTMA.text())
		pj     = float(self.ventanaEV.editJLO.text())
		ps     = float(self.ventanaEV.editSLO.text())
		pnhr   = int(self.ventanaEV.editNHR.text())
		vcff   = int(self.ventanaEV.editFF.text())
		vcrf   = int(self.ventanaEV.editRFF.text())
		vcrt   = int(self.ventanaEV.editRET.text())
		vcte   = int(self.ventanaEV.editT.text())
		vcti   = int(self.ventanaEV.comboTC.currentIndex())
		vccvh  = int(self.ventanaEV.comboCVH.currentIndex())
		vccvm  = int(self.ventanaEV.comboCVM.currentIndex())
		print isa
		ev = (run , fecha, vhifun, vhifis, vhiemo, vhitot, trr, trf, mrr, mrf, cfr, ni, tmf, tme, isa, ar, ppf1, ppf2, ppf3, ppl1, ppl2, ppl3, ppp1, ppp2, ppp3, po, tg, ti, ts, te, tce, ta, hpha, hec, hpp, hde, hrh, hpt, rr, ra, rs, ras, rt, ri, tmh, pj, ps, pnhr, vcff, vcrf, vcrt, vcte, vcti, vccvh, vccvm)
		guarda = CrudEV()
		guarda.insertarEvalVocal(ev)
		QtGui.QMessageBox.question(self,  'Alerta',  _fromUtf8('Evaluación Vocal agregada exitosamente.'))
		self.hide()
		
	def calcularVHI(self):
		vhifun = int(self.ventanaEV.spinFuncional.text())
		vhifis = int(self.ventanaEV.spinFisica.text())
		vhiemo = int(self.ventanaEV.spinEmocional.text())
		numero = vhifun + vhifis + vhiemo
		#print numero
		self.ventanaEV.lcdTotal.display(numero)
		#return numero

	def calcularISA(self):
		tmf = float(self.ventanaEV.spinTMF.text())
		tme = float(self.ventanaEV.spinTME.text())
		#var = float(tmf/tme)
		var = float("{0:.2f}".format(tmf/tme))
		self.ventanaEV.lcdNumber.display(str(var))

	def calcularPTH(self):
		hpha   = int(self.ventanaEV.spinHPHA.text())
		hec    = int(self.ventanaEV.spinHEC.text())
		hpp    = int(self.ventanaEV.spinHPP.text())
		hde    = int(self.ventanaEV.spinHDE.text())
		hrh    = int(self.ventanaEV.spinHRH.text())
		self.ventanaEV.lcdHPT.display(int(hpha+hec+hpp+hde+hrh))

#def main():
#	app = QtGui.QApplication(sys.argv)
#	ventana = Evaluacion("22.333.444-7")
#	ventana.show()
#	sys.exit(app.exec_())
#
#if __name__=="__main__":
#	main()
