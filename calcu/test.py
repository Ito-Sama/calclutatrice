
#Chargement des modules 

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import *


Debug = 1

def OnClik_OM_BoutonAjouter(event):
    if Debug ==1 : print('OnClik_OM_BoutonAjouter')
    tk.messagebox.showerror('itre', 'Indicatif inconnu',parent=fenetre)


fenetre = tk.Tk()
fenetre.geometry("1127x558+51+0")
fenetre.minsize(120, 1)
fenetre.maxsize(1284, 701)
fenetre.resizable(1,  1)

fenetre.Button_OM_Ajouter = tk.Button(fenetre)
fenetre.Button_OM_Ajouter.place(relx=0.475, rely=0.846, height=24, width=67 , bordermode='ignore')
fenetre.Button_OM_Ajouter.configure(text="Ajouter")


# Click Bouton
fenetre.Button_OM_Ajouter.bind('<Button-1>', OnClik_OM_BoutonAjouter)


fenetre.mainloop()