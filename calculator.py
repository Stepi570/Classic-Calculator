import tkinter as tk
from tkinter import messagebox

root = tk.Tk() #Создание окна
root.title("Калькулятор") #Название приложения
root.geometry("315x340")

vvod=tk.Entry(root, font=("Arial", 24),width=13)
vvod.pack(pady=15)
vvod.place(x=5,y=5)
vvod.insert(0, "")

def steretD():
    vvod.delete(0, tk.END)

def sevenD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"7")

def eightD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"8")
def nineD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"9")
def divideD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"%")

def fourD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"4")
def fiveD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"5")
def sixD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"6")
def multiplyD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"*")
def oneD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"1")
def twoD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"2")
def threeD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"3")
def minusD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"-")
def zeroD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"0")
def dotD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+".")
def exactlyD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    x=x.replace("%", "/")
    vvod.insert(0, eval(x))
def plusD():
    x=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, x+"+")


steret=tk.Button(root,text="АС", command=steretD, bg="#ff6df8",width=7, height=2)
steret.pack()
steret.place(x=245,y=5)

seven=tk.Button(root,text="7", command=sevenD, bg="#ff6df8",width=7, height=3)
seven.pack()
seven.place(x=5,y=70)

eight=tk.Button(root,text="8", command=eightD, bg="#ff6df8",width=7, height=3)
eight.pack()
eight.place(x=85,y=70)

nine=tk.Button(root,text="9", command=nineD, bg="#ff6df8",width=7, height=3)
nine.pack()
nine.place(x=165,y=70)

divide=tk.Button(root,text="%", command=divideD, bg="#ff6df8",width=7, height=3)
divide.pack()
divide.place(x=245,y=70)

four=tk.Button(root,text="4", command=fourD, bg="#ff6df8",width=7, height=3)
four.pack()
four.place(x=5,y=135)

five=tk.Button(root,text="5", command=fiveD, bg="#ff6df8",width=7, height=3)
five.pack()
five.place(x=85,y=135)

six=tk.Button(root,text="6", command=sixD, bg="#ff6df8",width=7, height=3)
six.pack()
six.place(x=165,y=135)

multiply=tk.Button(root,text="х", command=multiplyD, bg="#ff6df8",width=7, height=3)
multiply.pack()
multiply.place(x=245,y=135)

one=tk.Button(root,text="1", command=oneD, bg="#ff6df8",width=7, height=3)
one.pack()
one.place(x=5,y=200)

two=tk.Button(root,text="2", command=twoD, bg="#ff6df8",width=7, height=3)
two.pack()
two.place(x=85,y=200)

three=tk.Button(root,text="3", command=threeD, bg="#ff6df8",width=7, height=3)
three.pack()
three.place(x=165,y=200)

minus=tk.Button(root,text="-", command=minusD, bg="#ff6df8",width=7, height=3)
minus.pack()
minus.place(x=245,y=200)

zero=tk.Button(root,text="0", command=zeroD, bg="#ff6df8",width=7, height=3)
zero.pack()
zero.place(x=5,y=265)

dot=tk.Button(root,text=".", command=dotD, bg="#ff6df8",width=7, height=3)
dot.pack()
dot.place(x=85,y=265)

exactly=tk.Button(root,text="=", command=exactlyD, bg="#ff6df8",width=7, height=3)
exactly.pack()
exactly.place(x=165,y=265)

plus=tk.Button(root,text="+", command=plusD, bg="#ff6df8",width=7, height=3)
plus.pack()
plus.place(x=245,y=265)














root.mainloop()