# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import Tkinter
from dao import DAO
from user import User

class Janela:
	def __init__(self):
		self.top = Tkinter.Tk()
		self.Lb1 = Listbox(self.top)
		self.L1 = Label(self.top, text="Digite o username:")
		self.E1 = Entry(self.top, bd = 5)
		self.L2 = Label(self.top, text="Digite o email:")
		self.E2 = Entry(self.top, bd = 5)
		self.B = Tkinter.Button(self.top, text="Adicionar", command=self.eventoAdicionar)
		self.Br = Tkinter.Button(self.top, text="Remover", command=self.eventoRemover)
		self.L1.pack()
		self.E1.pack()
		self.L2.pack()
		self.E2.pack()
		self.dao = DAO()

		vet = self.dao.listar()
		for row in vet:
			self.Lb1.insert(row.username, row.email)
		self.Lb1.pack()

		self.B.pack()
		self.Br.pack()
		self.top.mainloop()

	def eventoAdicionar(self):
		if (str(self.E1.get()) > 0 and str(self.E2.get()) > 0):
			user = User(str(self.E1.get()), str(self.E2.get()))
			resultado = self.dao.inserir(user)
			if (resultado is True):
				self.Lb1.insert(self.Lb1.size(), user.email)
				tkMessageBox.showinfo("Foi...", "Adicionou...." )
			else:
				tkMessageBox.showinfo("Foi...", "Não Adicionou.......")
		else:
			tkMessageBox.showinfo("Foi...", "Não Adicionou.......")

	def eventoRemover(self):
	#print self.Lb1.curselection()
		if (len(self.Lb1.curselection())>0):
			print self.Lb1.get(self.Lb1.curselection()[0])
			self.dao.removerPorUsername(self.Lb1.get(self.Lb1.curselection()[0]))
			tkMessageBox.showinfo("Foi...", "Removeu....")
			self.Lb1.delete(self.Lb1.curselection())
		else:
			tkMessageBox.showinfo("Foi...", "Selecione um item....")


janela = Janela()