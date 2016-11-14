# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import Tkinter
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# configuracao do banco...
engine = create_engine("postgresql://postgres:postgres@localhost/test")

# criar o gerador da sessao
session = sessionmaker()
session.configure(bind=engine)

# classe que todo o modelo deve herdar
Base = declarative_base()

# modelo
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, name = "Igor"):
        self.name = name

# top
top = Tkinter.Tk()
# rotulo
L1 = Label(top, text="Digite o name:")
# caixa de texto
E1 = Entry(top, bd = 5)

# checkboxes
CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

# botao
def eventoAdicionar():
    s = session()
    s.add(Department(E1.get()))
    s.commit()
    tkMessageBox.showinfo("Foi...", "Adicionou...." )
    #s.delete(d)
    #s.commit()
    # se ele habilitou o checkbox
    print "Music selecionado?:"+str(CheckVar1.get())  #checked => 1
    # listar todos...   
    print s.query(Department).all()[0].name
    print s.query(Department).get(1).name

B = Tkinter.Button(top, text="Adicionar", command=eventoAdicionar)

# adicionando a tela
C1.pack()
C2.pack()
L1.pack()
E1.pack()
B.pack()

# criar o banco..
Base.metadata.create_all(engine)

# inicializando a tela...
top.mainloop()