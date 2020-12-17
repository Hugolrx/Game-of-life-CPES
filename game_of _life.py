from tkinter import *
from functools import partial
from time import sleep

root = Tk()
root.title("Le Jeu de la Vie")
# root.geometry("800x600")



file_entry = Entry(root)


def change_col(bouton) :
    if bouton.cget("bg") == "white" :
        bouton.configure(bg="black", activebackground="white")
    else :
        bouton.configure(bg="white", activebackground="black")


def boutons() :
    global dico

    for i in range(10) :
        for j in range(10) :

            dico[f"b{i}{j}"] = Button(root, padx=11, bg="white", activebackground="black", bd=1)
            dico[f"b{i}{j}"].configure(command=partial(change_col, dico[f"b{i}{j}"]))
            dico[f"b{i}{j}"].grid(row=i, column=j)

    launch = Button(root, text="  Go !  ")
    launch.configure(command=generation)
    launch.grid(row=5, column=50)



def generation(grid = None) :
    global dico

    if grid == None :
        for i in range(10) :
            for j in range(10) :
                bg_color, active_bg_color = dico[f"b{i}{j}"].cget("bg"), dico[f"b{i}{j}"].cget("activebackground")


    for i in range(len(grid)) :
        for j in range(len(grid[0])) :

            if grid[i][j] == 0 :
                color = "white"
            else :
                color = "black"

            dico[f"b{i}{j}"] = Label(root, padx=11, bg=color)

            dico[f"b{i}{j}"].grid(row=i, column=j)



def update(grid) :
    global dico

    for i in range(len(grid)) :
        for j in range(len(grid[0])) :

            if grid[i][j] == 0 :
                color = "white"
            else :
                color = "black"

            dico[f"b{i}{j}"].configure(bg=color)


dico = {}

boutons()

# generation([[0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0]])
#
#
# update([[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 1, 0, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0]])






root.mainloop()
























