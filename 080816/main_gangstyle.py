from gangstyle import *
from pacote_pessoa import *

"""
pessoa = PessoaFisica(None, "Everton", "safadao")
pessoaDAO = PessoaFisicaDAO()
pessoaDAO.inserir(pessoa)
"""

pessoaDAO = PessoaFisicaDAO()
pessoaDAO.excluir(8)



pessoaDAO = PessoaFisicaDAO()
lista = pessoaDAO.listar()
for i in range(0, len(lista)):
	print lista[i].nome
