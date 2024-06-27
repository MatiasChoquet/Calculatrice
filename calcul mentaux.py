#calcul mentaux.exe
import random
import tkinter as tk

def click():
    name = entry.get()
    Label.config(text="Bonjour " + name)


# def fenêtre
Fenetre = tk.Tk()
Fenetre.title('Mental\'eau')
Fenetre.geometry("800x400")


# def label
Label = tk.Label(Fenetre, text='Calcul Mental', 
font=("Arial", 20))
Label.pack()


# def frame
frame = tk.Frame(Fenetre, width=800, height=25)
frame.pack()


# def entry
entry = tk.Entry(Fenetre)
entry.pack()



# def frame
frame = tk.Frame(Fenetre, width=800, height=25)
frame.pack()


# def button
button = tk.Button(Fenetre, text='Valider la réponse',
width=15,
height=3,
command=click)
button.pack()


Fenetre.mainloop()










# fonction questions
def questions(x,y,z):
    print('Quel est la valeur de ',x, ' fois',y,' ? : ', end=' ')
    if z == int(input('')):
        print('La réponse est correct')
        return(1)
    else:
        print('La réponse est incorrect')
        return(0)


b = 0

#for i in range(0,2):
    #x = random.randint(0, 100)
    #y = random.randint(0, 100)
    #z = x*y
    #b = b + questions(x,y,z)
#print('Le ratio est de ',b, ' bonne(s) réponse(s) sur', i+1,' question(s).')



