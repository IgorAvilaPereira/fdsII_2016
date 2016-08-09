class Pessoa:
	def __init__(self, id = 0, nome = ""):
		self.id = id
		self.nome = nome
	def imprime(self):
		print "=============="
		print "Imprime do PAI:::InriCristo"
		return self.nome

class PessoaFisica(Pessoa):
	
	def __init__(self, id = None, nome = "", cpf = ""):
		Pessoa.__init__(self, id, nome)
		self.cpf = cpf
	def chamaImprime(self):
		# imprime do pai em vez do proprio imprime que foi reescrito
		return Pessoa.imprime(self) 
	def imprime(self):
		print "=============="
		print "Imprime do Filho:::PessoaFisica"
		return self.nome + ":"+ self.cpf