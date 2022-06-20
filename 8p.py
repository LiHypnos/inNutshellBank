from classe_cliente import *
from classe_conta import *
from tkinter import *
rp=['','','']
c=[]
p1 = Cliente(nome='Mateus', cpf='12345678', dataNasc='06/05/1988')
c1 = Conta(p1, num='123-4')
rp = Cliente(nome='Lian', cpf='12345679', dataNasc='04/08/2004')
c = Conta(rp,num='123-8')
rp = Cliente(nome='Emanuel', cpf='12345671', dataNasc='04/08/2004')
c= Conta(rp,num='1236')
p2 = Cliente(nome='Rodrigo', cpf='12345690', dataNasc='02/04/1987')
c2 = Conta(p2, num='123-6')
print(len(c))
c1.deposito(500)
c1.transfere_para(50,c2)
#c[len()].deposito(500)
#c[len(1)].transfere_para(60,c1)

#c[len(1)].deposito(600)

#c[len(1)].extrato()
c1.extrato()
c2.extrato()
