import Posicionamento
from tkinter import *
import tkinter as tk
from tkcalendar import *

#>>>>definindo algumas classes


#formatar cpf
def format_cpf(event=None):
    text = ent2.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    ent2.delete(0, "end")
    ent2.insert(0, new_text)

def format_cpfF(event=None):
    text = cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    cpf.delete(0, "end")
    cpf.insert(0, new_text)

#formatar data
def format_data(event=None):
    text = ent2.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 3]:
            new_text += text[index] + "/"
        else:
            new_text += text[index]

    ent2.delete(0, "end")
    ent2.insert(0, new_text)
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
    fc.forget()
    f0.pack()


def abrir():
    f0.forget()
    fc.pack()
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
    btdc.place(width=300, height=50, x=400, y=592)
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
    fc.forget()
    f7.pack()
    label6.pack()
    btnc.place(width=267, height=48, x=432, y=623)
    nome.place(width=604, height=31, x=178, y=358)
    cpf.place(width=402, height=29, x=152, y=425)
    dat.place(width=165, height=19, x=396, y=495)
    bb7.place(width=26, height=20, x=854, y=5)
    bubu.place(width=168, height=24, x=393, y=491)
    lub.place(width=173, height=43, x=391, y=523)
def ver():
    fc.forget()
    f8.pack()
    label7.pack()
    opt.place(width=83, height=20, x=537, y=244)
    optp.place(width=88, height=28, x=326, y=407)
    bb8.place(width=26, height=20, x=854, y=5)

def conf():
    fc.forget()
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
fc=Frame(root, bg='Black', border=0)
#criação dos itens f0 (inicio)
imagep = PhotoImage(file=r"C:\Users\889875\Downloads\nix\1.png")
#imagep = PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\1.png")
label=Label(f0, image=imagep)
btn=Button(f0, text='Login Cliente',font='Arial 20', bg='#350252', foreground='White', command=login)
btn2=Button(f0, text='Login Funcionário', font='Arial 28', bg='#350252', foreground='White',command=abrir)

#criação dos itens labell
imagepx = PhotoImage(file=r"C:\Users\889875\Downloads\nix\2.png")
#imagepx = PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\2.png")
pabelp=Label(fc, image=imagepx)
imagepxz = PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\lacr (1).png")
imagepxz1 = PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\lacr (2) (1).png")
imageula = PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\conf (1).png")
btp=Button(fc, text='Verificação', font='Arial 24', bg='#a6033f', foreground='White', command=ver, image=imagepxz)
btb=Button(fc, text='Criar uma conta', font='Arial 24', bg='#a6033f', foreground='White', command=cad, image=imagepxz1)
btv=Button(fc, text='Configurar Contas', font='Arial 24', bg='#a6033f', foreground='White', command=conf, image=imageula)
bb=Button(fc, text='<', font='Arial 20', bg='#60078c', foreground='White', command=home1)

#criação dos itens f1
imagepp= PhotoImage(file=r"C:\Users\889875\Downloads\nix\7.png")
#imagepp= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\7.png")
labelv=Label(f1, image=imagepp)
imagepxx = PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\IN (2) (1).png")
btlo=Button(f1, text='Entrar', font='Arial 24', bg='#5012c4', foreground='White', command=entrar,image=imagepxx)
ent1=Entry(f1, font='Arial 22', bg='#5012c4',foreground='White')
ent2=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
ent2.bind('<KeyRelease>', format_cpf)
ent3=Entry(f1, font='Arial 22', bg='#5012c4', foreground='White')
bb1=Button(f1, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f2
imagex= PhotoImage(file=r"C:\Users\889875\Downloads\nix\8.png")
#imagex= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\8.png")
label1=Label(f2, image=imagex)
imagedas= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\FAZ (1).png")
btd=Button(f2, text='Fazer Depósito', font='Arial 24', bg='#d020f7', foreground='White',command=deposito, image=imagedas)
imagedasy= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\his (2) (1).png")
bts=Button(f2, text='Fazer um Saque', font='Arial 22', bg='#d020f7', foreground='White', command=saque, image=imagedasy)
imagedasx= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\his (1).png")
bth=Button(f2, text='Ver Historico\nde\nTransações', font='Arial 24', bg='#d020f7', image=imagedasx, foreground='White', command=histo)
imagedasz= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\TRANS (1).png")
btt=Button(f2, text='Fazer uma Transferência', image=imagedasz, font='Arial 22', bg='#d020f7', foreground='White', command=trans)
labelpp=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
labelpb=Label(f2, font='Arial 20', bg='#5012c4', foreground='White')
bb2=Button(f2, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)


#criação dos itens f3
images= PhotoImage(file=r"C:\Users\889875\Downloads\nix\9.png")
#images= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\9.png")
label2=Label(f3, image=images)
imagescs= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\confirmar (2) (1).png")
val=Entry(f3, font='Arial 16', bg='#f507bd', foreground='White')
btdc=Button(f3, text='Realizar Depósito', font='Arial 22', bg='#ab0eb0', foreground='White', image=imagescs)
bb3=Button(f3, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#criação dos itens f4
imaged= PhotoImage(file=r"C:\Users\889875\Downloads\nix\10.png")
#imaged= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\10.png")
label3=Label(f4, image=imaged)
valp=Entry(f4, font='Arial 16',bg='#f507bd', foreground='White')
btds=Button(f4, text='Realizar Saque', font='Arial 22', bg='#ab0eb0', foreground='White', image=imagescs)
bb4=Button(f4, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f5
imaget= PhotoImage(file=r"C:\Users\889875\Downloads\nix\11.png")
#imaget= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\11.png")
label4=Label(f5, image=imaget)
vao=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
vae=Entry(f5, font='Arial 16',bg='#f507bd', foreground='White')
imagetx= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\confirmar (2) (2).png")
btdt=Button(f5, text='Realizar\nTransação', font='Arial 20', bg='#ab0eb0', foreground='White', image=imagetx)
bb5=Button(f5, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f6
imageh= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\12.png")
#imageh= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\12.png")
label5=Label(f6, image=imageh)
lus=Label(f6, font='Arial 10', background='#561fed')
lib=Entry(f6, font='Arial 10', bg='#561fed')
bb6=Button(f6, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f7
imagec= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\3.png")
#imagec= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\nix.png")
label6=Label(f7, image=imagec)
imagecc= PhotoImage(file=r"C:\Users\889875\PycharmProjects\Attt\conf (2) (1).png")
btnc=Button(f7, text='Criar Conta', font='Arial 20', bg='#ab0eb0', foreground='White', image=imagecc)
nome=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
cpf=Entry(f7, font='Arial 20',background='#561fed', foreground='White')
cpf.bind('<KeyRelease>', format_cpfF)
dat=Label(f7, font='Arial 15', background='#561fed', foreground='White')
bb7=Button(f7, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)

#Criação dos itens f8
imagev= PhotoImage(file=r"C:\Users\889875\Downloads\nix\4.png")
#imagev= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\4.png")
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
#imager= PhotoImage(file=r"C:\Users\Arlete\PycharmProjects\Attt\5.png")
label8=Label(f9, image=imager)
bb9=Button(f9, text='<', font='Arial 20', bg='#60078c', foreground='White',command=home1)




#verificar os pixels
root.bind('<Button-1>', Posicionamento.inicio_place)
root.bind('<ButtonRelease-1>', lambda arg: Posicionamento.fim_place(arg, root))
root.bind('<Button-2>', lambda arg: Posicionamento.para_geometry(root))

#data

lub = Label(f7,text='').place(width=173, height=43, x=391, y=523)
def Dater():
    global cal
    def getDate():
        date=cal.get_date()
        print(date)
    cal.place(width=267, height=204, x=580, y=407)
    lub['text']=str()date
    bubub=Button(f7,text='Confirmar Seleção', bg='purple', activeforeground='Black' , foreground='white', command=getDate).place(width=168, height=24, x=393, y=491)

cal=Calendar(f7, selectmode='day', date_pattern="dd-mm-y")
bubu=Button(f7, text='Confirmar Seleção', command=Dater)

lub = Label(f7,text=cal.get_date(),foreground='white', bg='black')




#rodando
f0.pack()
label.pack()
btn.place(width=183, height=65, x=627, y=225)
btn2.place(width=305, height=73, x=583, y=574)
root.mainloop()