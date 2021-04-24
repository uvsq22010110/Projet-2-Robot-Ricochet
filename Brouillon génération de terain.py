import tkinter as tk

import random as rd

HAUTEUR = 640
LARGEUR = 640
COULEUR_FOND = "navajo white"
COTE = 40
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

COULEUR_QUADRILLAGE = "black"
COULEUR_ROBOT1 = "red"
COULEUR_ROBOT2 = "green"
COULEUR_ROBOT3 = "blue"
COULEUR_ROBOT4 = "yellow"
COULEUR_CIBLE = "aleatoire"

def quadrillage():
    global COULEUR_QUADRILLAGE
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADRILLAGE)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADRILLAGE)
        x += COTE


def coord_to_lg(x, y):
    
    return x // COTE, y // COTE


def bordure():
    mur1 = canvas.create_line(0,0,0,639, fill="black", width = '9')
    mur2 = canvas.create_line(0,0,639,0, fill="black", width = '9')
    mur3 = canvas.create_line(639,0,639,639, fill="black", width = '9')
    mur4 = canvas.create_line(0,639,639,639, fill="black", width = '9' )

    
    


root = Tk()
canvas = Canvas(root, width=640, height=640, borderwidth=0, highlightthickness=0, bg = COULEUR_FOND)
canvas.grid(column = 1, row = 0)
canvas.pack()


quadrillage()
bordure()    
root.mainloop()
