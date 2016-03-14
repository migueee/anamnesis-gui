# -*- encoding: utf-8 -*-
import sqlite3

# TODO: Obtener ruta local de forma dinamica
# db = sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/ANAMNESIS')

def conectate():    
	return sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/dungunvoz.db')

class CrudSyC(object):
	"""Clase encargada de interactuar con la tabla SINTOMATOLOGIA que almacena la información de SINTOMATOLOGÍA Y CONDUCTAS de la anamnesis"""
	
	def insertarSintomatologia(self, lista):
		"""metodo que ingresa una nueva sintomatología a la base de datos para un determinado paciente."""
		basedatos = conectate()
		consulta = basedatos.cursor()
		#print(lista)
		sql = """INSERT INTO SINTOMATOLOGIA (RUN, FECHA, SINTOMAVOCAL1, DESCRSINTOMA1, SINTOMAVOCAL2, DESCRSINTOMA2, SINTOMAVOCAL3, DESCRSINTOMA3, SINTOMAVOCAL4, DESCRSINTOMA4, OSINTOMA1, DESCROSINTOMA1, OSINTOMA2, DESCROSINTOMA2, OSINTOMA3, DESCROSINTOMA3, OSINTOMA4, DESCROSINTOMA4, ANTMEDICOS, MEDICAMENTOS, CABUSOVOCAL1, DETALLECONDUCTA1, CABUSOVOCAL2, DETALLECONDUCTA2, CABUSOVOCAL3, DETALLECONDUCTA3, CABUSOVOCAL4, DETALLECONDUCTA4, HHDUERME) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		consulta.execute(sql,(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12],lista[13],lista[14],lista[15],lista[16],lista[17],lista[18],lista[19],lista[20],lista[21],lista[22],lista[23],lista[24],lista[25],lista[26],lista[27],lista[28]))
		basedatos.commit()
		consulta.close()
		basedatos.close()
		print "base de datos cerrada"
	
	#no tiene mayores validaciones por que el rut ya fue consultado en la función consultarRun()		
	def retornaSintomatologia(self, ids):
		basedatos = conectate()
		consulta = basedatos.cursor()
		sql = """SELECT * FROM sintomatologia WHERE ID = ?;"""
		print ids
		consulta.execute(sql, (int(ids),))
		data=consulta.fetchall()
		basedatos.commit()
		consulta.close()
		basedatos.close()
		return data
		
	def retornaIdFecha(self, run):
		basedatos = conectate()
		consulta  = basedatos.cursor()
		sql       = """SELECT ID, FECHA FROM sintomatologia WHERE RUN = (?) ORDER BY FECHA;"""
		consulta.execute(sql, (run,))
		data=consulta.fetchall()
		basedatos.commit()
		consulta.close()
		basedatos.close()
		return data
	
	def eliminarSintoma(self, ids):
		basedatos = conectate()
		consulta  = basedatos.cursor()
		sql       = """DELETE FROM sintomatologia WHERE ID = ?;"""
		print "se supone que eliminaste un sintoma"
		consulta.execute(sql, (int(ids),))
		basedatos.commit()
		consulta.close()
		basedatos.close()
		
