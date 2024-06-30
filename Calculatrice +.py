#calcul mentaux.exe
import random
import tkinter as tk
import customtkinter
import time

customtkinter.set_default_color_theme("green")

# def fenêtre
Fenetre = customtkinter.CTk()
Fenetre.title('Calculatrice +')

Donnée = " "
Last_Order = "None"
InMemory = []
Basic = []
Result = 0
Reset = 0
Erreur = 0
string_variable = tk.StringVar()
string_variable.set(Donnée)

def police(police):
    if len(police) > 15:
        return float(len(police)/1.05)
    else:
        return 36

def set0():
    Donnée = " "
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def set0bis():
    Donnée = " "
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add1():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "1"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')
    

def add2():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "2"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')
    

def add3():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "3"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add4():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "4"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add5():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "5"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add6():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "6"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add7():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "7"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add8():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "8"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add9():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "9"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def add0():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "0"
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def addpoint():
    global Reset
    if len(InMemory) != len(Basic):
        set0()
        Basic.append(InMemory[-1])
    if Reset != 0:
        set0()
        Reset = 0
    Donnée = string_variable.get()
    Donnée += "."
    string_variable.set(Donnée)
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

def Last_Order_Change():
    global  Last_Order, Result, InMemory, Basic, Reset, Erreur
    if Last_Order == "Minus":
        Result -= InMemory[-1]
    elif Last_Order == "Plus":
        Result += InMemory[-1]
    elif Last_Order == "Fois":
        Result *= InMemory[-1]
    elif Last_Order == "Diviser":
        if InMemory[-1] == 0:
            InMemory, Basic, Erreur, Reset = [], [], 1, 1
            Last_Order = "None"
        else:
            Result /= InMemory[-1]
    elif Last_Order == "Puissance":
        try:
            Result **= InMemory[-1]
        except OverflowError:
            InMemory, Basic, Erreur, Reset = [], [], 2, 1
    else:
        Result += InMemory[-1]
    

def plus():
    global InMemory, Basic, Result, Last_Order
    InMemory.append(float(string_variable.get()))
    Last_Order_Change()
    Last_Order = "Plus"
    print(InMemory, Basic, Result, string_variable.get())

def moins():
    global InMemory, Basic, Result, Last_Order
    if len(InMemory) == 0 and (string_variable.get() == " " or string_variable.get() == "Error"):
        string_variable.set(Result)
    InMemory.append(float(string_variable.get()))
    Last_Order_Change() 
    Last_Order = "Minus"
    print(InMemory, Basic, Result, string_variable.get())

def fois():
    global InMemory, Basic, Result, Last_Order
    InMemory.append(float(string_variable.get()))
    Last_Order_Change()
    Last_Order = "Fois"
    print(InMemory, Basic, Result, string_variable.get())

def diviser():
    global InMemory, Basic, Result, Last_Order
    InMemory.append(float(string_variable.get()))
    Last_Order_Change()
    Last_Order = "Diviser"
    print(InMemory, Basic, Result, string_variable.get())

def puissance():
    global InMemory, Basic, Result, Last_Order
    InMemory.append(float(string_variable.get()))
    Last_Order_Change()
    Last_Order = "Puissance"
    print(InMemory, Basic, Result, string_variable.get())

def equal():
    global InMemory, Basic, Result, Last_Order, Reset, Erreur
    InMemory.append(float(string_variable.get()))
    Last_Order_Change()
    Last_Order = "None"
    if Erreur == 0:
        string_variable.set(str(round(Result,3)))
    elif Erreur == 1:
        string_variable.set("Division by 0 is impossible")
    elif Erreur == 2:
        string_variable.set('Error, number too large')
    label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', police(string_variable.get())))
    label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')
    InMemory, Basic, Result, Reset, Erreur = [], [], 0, 1, 0



#def grille
Fenetre.grid_rowconfigure(0, weight=6)
Fenetre.grid_rowconfigure(1, weight=1)
Fenetre.grid_rowconfigure(2, weight=1)
Fenetre.grid_rowconfigure(3, weight=1)
Fenetre.grid_rowconfigure(4, weight=1)
Fenetre.grid_rowconfigure(5, weight=1)


Fenetre.grid_columnconfigure(0, weight=1, uniform="same_group")
Fenetre.grid_columnconfigure(1, weight=1, uniform="same_group")
Fenetre.grid_columnconfigure(2, weight=1, uniform="same_group")
Fenetre.grid_columnconfigure(3, weight=1, uniform="same_group")

label = customtkinter.CTkLabel(master= Fenetre,text=string_variable.get(), anchor='se', corner_radius=10,font=('Arial', 36), wraplength=72)
label.grid(column=0, row=0, columnspan= 4, padx = 15, pady = 15, sticky='nsew')

b1=customtkinter.CTkButton(Fenetre, text ="C", font=('Arial', 25, "bold"), command=set0)
b1.grid(column=0, row=1, padx=10, pady=15, sticky='nesw')
b2=customtkinter.CTkButton(Fenetre, text="^", font=('Arial', 25, "bold"), command=puissance)
b2.grid(column=1, row=1, padx=10, pady=15, sticky='nesw')
b3=customtkinter.CTkButton(Fenetre, text="/", font=('Arial', 25, "bold"), command=diviser)
b3.grid(column=2, row=1, padx=10, pady=15, sticky='nesw')
b4=customtkinter.CTkButton(Fenetre, text="*", font=('Arial', 25, "bold"), command=fois)


b4.grid(column=3, row=1, padx=10, pady=15, sticky='nesw')
b5=customtkinter.CTkButton(Fenetre, text="7", font=('Arial', 25, "bold"), command=add7)
b5.grid(column=0, row=2, padx=10, pady=15, sticky='nesw')
b6=customtkinter.CTkButton(Fenetre, text="8", font=('Arial', 25, "bold"), command=add8)
b6.grid(column=1, row=2, padx=10, pady=15, sticky='nesw')
b7=customtkinter.CTkButton(Fenetre, text="9", font=('Arial', 25, "bold"), command=add9)
b7.grid(column=2, row=2, padx=10, pady=15, sticky='nesw')
b8=customtkinter.CTkButton(Fenetre, text="-", font=('Arial', 25, "bold"), command=moins)


b8.grid(column=3, row=2, padx=10, pady=15, sticky='nesw')
b9=customtkinter.CTkButton(Fenetre, text="4", font=('Arial', 25, "bold"), command=add4)
b9.grid(column=0, row=3, padx=10, pady=15, sticky='nesw')
b10=customtkinter.CTkButton(Fenetre, text="5", font=('Arial', 25, "bold"), command=add5)
b10.grid(column=1, row=3, padx=10, pady=15, sticky='nesw')
b11=customtkinter.CTkButton(Fenetre, text="6", font=('Arial', 25, "bold"), command=add6)
b11.grid(column=2, row=3, padx=10, pady=15, sticky='nesw')
b12=customtkinter.CTkButton(Fenetre, text="+", font=('Arial', 25, "bold"), command=plus)
b12.grid(column=3, row=3, padx=10, pady=15, sticky='nesw')

b13=customtkinter.CTkButton(Fenetre, text="1", font=('Arial', 25, "bold"), command=add1)
b13.grid(column=0, row=4, padx=10, pady=15, sticky='nesw')
b14=customtkinter.CTkButton(Fenetre, text="2", font=('Arial', 25, "bold"), command=add2)
b14.grid(column=1, row=4, padx=10, pady=15, sticky='nesw')
b15=customtkinter.CTkButton(Fenetre, text="3", font=('Arial', 25, "bold"), command=add3)
b15.grid(column=2, row=4, padx=10, pady=15, sticky='nesw')
b16=customtkinter.CTkButton(Fenetre, text="=", font=('Arial', 25, "bold"), command=equal)
b16.grid(column=3, row=4,rowspan = 2, padx=10, pady=15, sticky='nesw')


b17=customtkinter.CTkButton(Fenetre, text="0", font=('Arial', 25, "bold"), command=add0)
b17.grid(column=0, row=5, columnspan = 2, padx=10, pady=15, sticky='nesw')
b18=customtkinter.CTkButton(Fenetre, text=".", font=('Arial', 25, "bold"), command=addpoint)
b18.grid(column=2, row=5, padx=10, pady=15, sticky='nesw')




Fenetre.geometry("400x550")
Fenetre.resizable(False, False)

Fenetre.mainloop()
