# -*- coding: utf8 -*-
from matematica import *

def agoravai(self, x):
	return x

mauricio = Pessoa("maumauSafadao ;)")
print dir(mauricio)
Pessoa.agoravai = agoravai
print dir(mauricio)
print mauricio.agoravai("wesley")

"""
x = PessoaFisica("igor", "cpfdoigor")
print x.nome
print x.cpf
print x.chamaImprime()
print x.imprime()
"""

"""
nro1 = int(raw_input("Digite o nro1:"))
nro2 = int(raw_input("Digite o nro2:"))

print str(soma(nro1, nro2))

print str(sum([1,2,3,4]))
print str(somaLista([1,2,3,4]))
"""
"""
nro1 = 3
nro2 = 5
biblioteca = BibliotecaMatematica(nro1,nro2)
print isinstance(biblioteca, BibliotecaMatematica)
#print biblioteca
print str(biblioteca.divisao())
"""
"""
print "Potenciação:"+ str(biblioteca.potenciacao())
print biblioteca.oiOlaPublico()
vetor1 = Vetor(1,2)
vetor2 = Vetor(2,1)
vetorR = vetor1 + vetor2
print vetorR
#print str(vetorR.x) + "," + str(vetorR.y)
"""