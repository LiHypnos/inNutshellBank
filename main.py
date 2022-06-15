import Posicionamento
from tkinter import *
import tkinter as tk
import pa
#comandos indispensaveis

def home1():
    f2.forget()
    f1.forget()
    f3.forget()
    f4.forget()
    f5.forget()
    f6.forget()
    f7.forget()
    f8.forget()
    f9.forget()
    f0.pack()


def abrir():
    f0.forget()
    f1.pack()
    pabelp.pack()
    btp.place(width=296, height=48, x=136, y=275)
    btb.place(width=248, height=69, x=152, y=392)
    btv.place(width=282, height=71, x=145, y=512)
    bb1.place(width=26, height=20, x=854, y=5)
def login():
    f0.forget()
    f1.pack()
    labelv.pack()
    btlo.place(width=152, height=52, x=474, y=536)
    bth.place(width=312, height=101, x=358, y=202)
    btt.place(width=332, height=69, x=443, y=500)
    ent1.place(width=621, height=36, x=170, y=297)
    ent2.place(width=421, height=38, x=144, y=365)
    ent3.place(width=176, height=27, x=273, y=430)
    bb1.place(width=26, height=20, x=854, y=5)

def entrar():
    f1.forget()
    f2.pack()
    label1.pack()
    btd.place(width=224, height=70, x=52, y=235)
    bts.place(width=220, height=68, x=164, y=519)
    labelpp.place(width=186, height=34, x=412, y=709)
    labelpb.place(width=157, height=27, x=855, y=233)
    bb2.place(width=26, height=20, x=854, y=5)

def deposito():
    f2.forget()
    f3.pack()
    label2.pack()
    btdc.place(width=300, height=40, x=400, y=592)
    val.place(width=137, height=36, x=484, y=288)
    bb3.place(width=26, height=20, x=854, y=5)
def saque():
    f2.forget()
    f4.pack()
    label3.pack()
    btds.place(width=243, height=40, x=743, y=297)
    valp.place(width=194, height=33, x=426, y=291)
    bb4.place(width=26, height=20, x=854, y=5)
def trans():
    f2.forget()
    f5.pack()
    label4.pack()
    btdt.place(width=165, height=73, x=394, y=614)
    vao.place(width=142, height=32, x=512, y=284)
    vae.place(width=137, height=26, x=482, y=416)
    bb5.place(width=26, height=20, x=854, y=5)
def histo():
    f2.forget()
    f6.pack()
    label5.pack()
    lus.place(width=489, height=547, x=32, y=126)
    lib.place(width=355, height=225, x=606, y=228)
    bb6.place(width=26, height=20, x=854, y=5)
def cad():
    f1.forget()
    f7.pack()
    label6.pack()
    btnc.place(width=267, height=48, x=432, y=623)
    nome.place(width=604, height=31, x=178, y=358)
    cpf.place(width=402, height=29, x=152, y=425)
    dat.place(width=165, height=19, x=396, y=495)
    bb7.place(width=26, height=20, x=854, y=5)
def ver():
    f1.forget()
    f8.pack()
    label7.pack()
    opt.place(width=83, height=20, x=537, y=244)
    optp.place(width=88, height=28, x=326, y=407)
    bb8.place(width=26, height=20, x=854, y=5)
def conf():
    f1.forget()
    f9.pack()
    label8.pack()
    bb9.place(width=26, height=20, x=854, y=5)



#criação da janela
root=Tk()
root.title('NIX')
root.geometry('400x200+100+500')
root.minsize(width=1023, height=755)
root.maxsize(width=1023, height=755)
root.config(bg=('white'))

#criação dos frames
f0=Frame(root, bg='Black', border=0)
f1=Frame(root, bg='black', border=0)
f2=Frame(root, bg='Black', border=0)
f2=Frame(root, bg='Black', border=0)
f3=Frame(root, bg='Black', border=0)
f4=Frame(root, bg='Black', border=0)
f5=Frame(root, bg='Black', border=0)
f6=Frame(root, bg='Black', border=0)
f7=Frame(root, bg='black', border=0)
f8=Frame(root, bg='Black', border=0)
f9=Frame(root, bg='Black', border=0)

#criação dos itens f0 (inicio)
imagep = PhotoImage(file=r"C:\Users\889875\Downloads\nix\1.png")
label=Label(f0, image=imagep)
btn=Button(f0, text='Login Cliente',font='Arial 20', bg='#350252', foreground='White', command=login)
btn2=Button(f0, text='Login Funcionário', font='Arial 28', bg='#350252', foreground='White',command=abrir)

#criação dos itens labell
imagepx = PhotoImage(file=r"C:\Users\889875\Downloads\nix\2.png")
pabelp=Label(f1, image=imagepx)
btp=Button(f1, text='Verificação', font='Arial 24', bg='#a6033f', foreground='White', command=ver)
btb=Button(f1, text='Criar uma conta', font='Arial 24', bg='#a6033f', foreground='White', command=cad)
btv=Button(f1, text='Configurar Contas', font='Arial 24', bg='#a6033f', foreground='White', command=conf)
bb=Button(f1, text='<', font='Arial 20', bg='#a6033f', foreground='White', command=home1)

#criação dos itens f1
imagepp= PhotoImage(file=r"C:\Users\889875\Downloads\nix\7.png")
labelv=Label(f1, image=imagepp)
btlo=Button(f1, text='Entrar', font='Arial 24', bg='#5012c4', foreground='White', command=entrar)
ent1=Entry(f1, font='Arial 22', bg='#5012c4',foreground='White')
ent2=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
ent3=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
bb1=Button(f1, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f2
imagex= PhotoImage(file=r"C:\Users\889875\Downloads\nix\8.png")
label1=Label(f2, image=imagex)
btd=Button(f2, text='Fazer Depósito', font='Arial 24', bg='#d020f7', foreground='White',command=deposito)
bts=Button(f2, text='Fazer um Saque', font='Arial 22', bg='#d020f7', foreground='White', command=saque)
bth=Button(f2, text='Ver Historico\nde\nTransações', font='Arial 24', bg='#d020f7', foreground='White', command=histo)
btt=Button(f2, text='Fazer uma Transferência', font='Arial 22', bg='#d020f7', foreground='White', command=trans)
labelpp=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
labelpb=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
bb2=Button(f2, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)


#criação dos itens f3
images= PhotoImage(file=r"C:\Users\889875\Downloads\nix\9.png")
label2=Label(f3, image=images)
val=Entry(f3, font='Arial 16', bg='#f507bd', foreground='White')
btdc=Button(f3, text='Realizar Depósito', font='Arial 22', bg='#ab0eb0', foreground='White')
bb3=Button(f3, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#criação dos itens f4
imaged= PhotoImage(file=r"C:\Users\889875\Downloads\nix\10.png")
label3=Label(f4, image=imaged)
valp=Entry(f4, font='Arial 16',bg='#f507bd', foreground='White')
btds=Button(f4, text='Realizar Saque', font='Arial 22', bg='#ab0eb0', foreground='White')
bb4=Button(f4, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f5
imaget= PhotoImage(file=r"C:\Users\889875\Downloads\nix\11.png")
label4=Label(f5, image=imaget)
vao=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
vae=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
btdt=Button(f5, text='Realizar\nTransação', font='Arial 20', bg='#ab0eb0', foreground='White')
bb5=Button(f5, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f6
imageh= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\12.png")
label5=Label(f6, image=imageh)
lus=Label(f6, font='Arial 10', background='#561fed')
lib=Entry(f6, font='Arial 10', bg='#561fed')
bb6=Button(f6, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f7
imagec= PhotoImage(file=r"C:\Users\889875\Downloads\nix\3.png")
label6=Label(f7, image=imagec)
btnc=Button(f7, text='Criar Conta', font='Arial 20', bg='#ab0eb0', foreground='White')
nome=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
cpf=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
dat=Label(f7, font='Arial 15', background='#561fed', foreground='White')
bb7=Button(f7, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f8
imagev= PhotoImage(file=r"C:\Users\889875\Downloads\nix\4.png")
label7=Label(f8, image=imagev)
list=['0']
olist=['0']
variable = tk.StringVar(f8)
variable.set(list[0])

opt = tk.OptionMenu(f8, variable, *list)
opt.config(text='Gênero', font=('Arial 10'), background='#450be9')

variablep = tk.StringVar(f8)
variablep.set(olist[0])

optp = tk.OptionMenu(f8, variablep, *olist)
optp.config(text='Gênero', font=('Arial 10'), background='#450be3')
bb8=Button(f8, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)

#Criação dos itens f9
imager= PhotoImage(file=r"C:\Users\889875\Downloads\nix\5.png")
label8=Label(f9, image=imager)
bb9=Button(f9, text='<', font='Arial 20', bg='#a6033f', foreground='White',command=home1)




#verificar os pixels
root.bind('<Button-1>', Posicionamento.inicio_place)
root.bind('<ButtonRelease-1>', lambda arg: Posicionamento.fim_place(arg, root))
root.bind('<Button-2>', lambda arg: Posicionamento.para_geometry(root))
#rodando
f0.pack()
label.pack()
btn.place(width=183, height=65, x=627, y=225)
btn2.place(width=305, height=70, x=583, y=574)
root.mainloop()