from sys import *

class BibliotecaMatematica:
	
	def __init__(self, nro1Monstro = 0, nro2SaiDaJaula = 0):
		self.nro1 = nro1Monstro
		self.nro2 = nro2SaiDaJaula
		
	def __oiOla(self):
		return "Oi...Birl!!! Comi p C@#R antes de sair de casa"

	def oiOlaPublico(self):
		return self.__oiOla()

	def soma(self):
		return self.nro1 + self.nro2

	def divisao(self):
		try:
			return self.nro1 / self.nro2
		except Exception, e:
			print "Deu xabum!!! Divisao por zero!!!"
			return 0
			#exit()
			#raise e	

	def potenciacao(self):
		return self.nro1**self.nro2

	def somaLista(self, lista = []):		
		resultado = 0
		for i in range(0, len(lista)):
			resultado += lista[i]
		return resultado

class Vetor:
	def __init__(self, nro1, nro2):		
		self.x = nro1
		self.y = nro2
	def __add__(self, vetor):
		vetorResultado = Vetor(self.x + vetor.x, self.y + vetor.y)		
		return vetorResultado
	"""
	def __repr__(self):
		return str(self.x) + "," + str(self.y)
	"""	