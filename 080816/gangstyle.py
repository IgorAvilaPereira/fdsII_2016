import psycopg2
from pacote_pessoa import *


class Conexao:
	def __init__(self):	
		# conectei...
		self.con = psycopg2.connect("dbname=aula080816 host=localhost user=postgres password=postgres")
		# abri o cursor
		self.cur = self.con.cursor()

	def fechar(self):
		# fechando o cursor
		self.cur.close()
		# fechando a conexao
		self.con.close()


class PessoaFisicaDAO:
	"""
	def __init__(self):		
	"""
	def listar(self):
		objConexao = Conexao()	
		objConexao.cur.execute("SELECT * FROM pessoa;")
		lista = []
		linhasRetornadas = objConexao.cur.rowcount
		i = 0
		while(i < linhasRetornadas):
			registro = objConexao.cur.fetchone()
			lista.append(PessoaFisica(registro[0],registro[1],registro[2]))
			i += 1
		objConexao.fechar()
		return lista 

	def excluir(self, id):
		# criar a conexao
		objConexao = Conexao()	
				
		# sql
		objConexao.cur.execute("DELETE FROM pessoa WHERE id = %s", [id])
		
		# comitando
		objConexao.con.commit()

		objConexao.fechar()

	def inserir(self, pessoaFisica):
		# abri cursor
		objConexao = Conexao()	
				
		# sql
		objConexao.cur.execute("INSERT INTO pessoa(nome, cpf) VALUES (%s,%s)", [pessoaFisica.nome,pessoaFisica.cpf])
		
		# comitando
		objConexao.con.commit()

		objConexao.fechar()
		
		
