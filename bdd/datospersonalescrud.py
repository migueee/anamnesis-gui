# -*- encoding: utf-8 -*-
import sqlite3


# TODO: Obtener ruta local de forma dinamica
# db = sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/ANAMNESIS')

def conectate(): 
	"""Devuelve el string con la conexión al archivo de sqlite"""   
	return sqlite3.connect('/home/macoi/sw/voz/dungun/anamnesis-gui/bdd/dungunvoz.db')

class Cruddp(object):
	"""Clase encargada de gestionar la tabla PACIENTE"""
	
	def insertarPaciente(self, lista):
		basedatos = conectate()
		consulta = basedatos.cursor()
		if self.consultarRun(lista[0]) == True:
			return False
		else:
			consulta.execute("""INSERT INTO paciente (RUN, NOMBRE, APELLIDO, FNACIMIENTO, OCUPACION, HHOCUPACION, OEXTRA, HHOEXTRA, CODAREA, FONO, EMAIL, MOTIVO) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11]))
			basedatos.commit()
			consulta.close()
			basedatos.close()
			return True
			
	def actualizarPaciente(self, lista):
		basedatos = conectate()
		consulta = basedatos.cursor()
		sql = """UPDATE paciente SET NOMBRE = ?, APELLIDO = ?, FNACIMIENTO = ?, OCUPACION = ?, HHOCUPACION = ?, OEXTRA = ?, HHOEXTRA = ?, CODAREA = ?, FONO = ?, EMAIL = ?, MOTIVO = ? WHERE RUN = ?;"""
		consulta.execute(sql,(lista[1],lista[2],lista[3],lista[4],int(lista[5]),lista[6],int(lista[7]),int(lista[8]),int(lista[9]),lista[10],lista[11],lista[0],))
		basedatos.commit()
		consulta.close()
		basedatos.close()
		
	def consultarRun(self, run):
		basedatos = conectate()
		consulta = basedatos.cursor()
		print(run)
		sql = """SELECT * FROM paciente WHERE RUN = (?);"""
		consulta.execute(sql, (run,))
		data=consulta.fetchall()
		basedatos.commit()
		consulta.close()
		basedatos.close()
		print(data)
		if (len(data) > 0):
			print("run encontrado con éxito")
			return True
		else:
			print("run no encontrado")
			return False
	
	#no tiene mayores validaciones por que el rut ya fue consultado en la función consultarRun()		
	def retornaPaciente(self, run):
		basedatos = conectate()
		consulta = basedatos.cursor()
		print(run)
		sql = """SELECT * FROM paciente WHERE RUN = (?);"""
		consulta.execute(sql, (run,))
		basedatos.commit()
		data=consulta.fetchall()
		consulta.close()
		basedatos.close()
		return data
		
	def retornaNombre(self, run):
		basedatos = conectate()
		consulta = basedatos.cursor()
		print(run)
		sql = """SELECT NOMBRE, APELLIDO FROM paciente WHERE RUN = (?)"""
		consulta.execute(sql, (run,))
		basedatos.commit()
		data=consulta.fetchall()
		consulta.close()
		basedatos.close()
		return data[0][0]+" "+data[0][1]
