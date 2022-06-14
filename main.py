import Posicionamento
from tkinter import *
import tkinter as tk
import pa

#criação da janela
root=Tk()
root.title('Windows Execute')
f1=Frame(root)
root.geometry('400x200+100+500')
root.minsize(width=1024, height=728)
root.maxsize(width=1024, height=728)
root.config(bg=('white'))
imagep = PhotoImage(file=r"C:\Users\889875\Downloads\nix\1.png")
label=Label(root, image=imagep)

btn=Button(label, text='Login Cliente',font='Arial 20', bg='Black', foreground='White', command=pa.lu.abrir())
btn2=Button(label, text='Login Funcionário', font='Arial 28', bg='Black', foreground='White')
imagepx = PhotoImage(file=r"C:\Users\889875\Downloads\nix\2.png")
pabelp=Label(f1, image=imagepx)



#verificar os pixels
root.bind('<Button-1>', Posicionamento.inicio_place)
root.bind('<ButtonRelease-1>', lambda arg: Posicionamento.fim_place(arg, root))
root.bind('<Button-2>', lambda arg: Posicionamento.para_geometry(root))

label.pack()
btn.place(width=183, height=65, x=627, y=212)
btn2.place(width=305, height=70, x=583, y=564)
root.mainloop()