# -*- encoding: utf-8 -*-
import sqlite3

# TODO: Obtener ruta local de forma dinamica
# db = sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/ANAMNESIS')

def conectate():    
	return sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/dungunvoz.db')

class CrudEV(object):
	"""Clase encargada de interactuar con la tabla EVALUACION que almacena la información de SINTOMATOLOGÍA Y CONDUCTAS de la anamnesis"""
	
	def insertarEvalVocal(self, lista):
		"""metodo que ingresa una nueva sintomatología a la base de datos para un determinado paciente."""
		basedatos = conectate()
		consulta = basedatos.cursor()
		print(lista)
		sql = """INSERT INTO EVALUACION (RUT, FECHA, VHIFUN, VHIFIS, VHIEMO, VHITOT, TRREPOSO, TRFONACION, MRREPOSO, MRFONACION, CORDFONORESP, NINSPIRACIONES, TMAXFONACION, TMAXESPIRACION, INDICESA, APOYORESP, POSPF1, POSPF2, POSPF3, POSPL1, POSPL2, POSPL3, POSPP1, POSPP2, POSPP3, POSOBS, TONICGRAL, TONICINFR, TONICSUPR, TONICERV, TONICESCA, TONICALTU, HIPERPHA, HIPEREDC, HIPERPDP, HIPERDEE, HIPERREH, HIPERPT, RASATIRON, RASATIASP, RASATISOP, RASATIAST, RASATITEN, RASATIINE, TMH, PAJITTER, PASHIMMER, PANHR, VOZCFF, VOZCRF, VOZCRTET, VOZCTESI, VOZCTIPO, VOZCCVH, VOZCCVM) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
		consulta.execute(sql,(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12],lista[13],lista[14],lista[15],lista[16],lista[17],lista[18],lista[19],lista[20],lista[21],lista[22],lista[23],lista[24],lista[25],lista[26],lista[27],lista[28],lista[29],lista[30],lista[31],lista[32],lista[33],lista[34],lista[35],lista[36],lista[37],lista[38],lista[39],lista[40],lista[41],lista[42],lista[43],lista[44],lista[45],lista[46],lista[47],lista[48],lista[49],lista[50],lista[51],lista[52],lista[53],lista[54]))
		basedatos.commit()
		consulta.close()
		basedatos.close()
		print "Evaluación vocal insertada con éxito"

	def retornaEvalVocal(self, ide):
		basedatos = conectate()
		consulta = basedatos.cursor()
		sql = """SELECT * FROM EVALUACION WHERE ID = (?);"""
		consulta.execute(sql, (int(ide),))
		data=consulta.fetchall()
		basedatos.commit()
		consulta.close()
		basedatos.close()
		return data
		
	def retornaIdFechaEV(self, run):
		basedatos = conectate()
		consulta  = basedatos.cursor()
		sql       = """SELECT ID, FECHA FROM EVALUACION WHERE RUT = (?) ORDER BY FECHA;"""
		consulta.execute(sql, (run,))
		data=consulta.fetchall()
		basedatos.commit()
		consulta.close()
		basedatos.close()
		return data
		
	def eliminarEvocal(self, ide):
		basedatos = conectate()
		consulta  = basedatos.cursor()
		sql       = """DELETE FROM EVALUACION WHERE ID = ?;"""
		consulta.execute(sql, (int(ide),))
		basedatos.commit()
		consulta.close()
		basedatos.close()
