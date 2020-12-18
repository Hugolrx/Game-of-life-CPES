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


def buttons() :
    global dico

    for i in range(30) :
        for j in range(30) :

            dico[f"b{i}{j}"] = Button(root, padx=12, bg="white", activebackground="black")
            dico[f"b{i}{j}"].configure(command=partial(change_col, dico[f"b{i}{j}"]))
            dico[f"b{i}{j}"].grid(row=i, column=j)

    dico["e"] = Entry(root, width = 30)
    dico["e"].grid(row=4, column=50)

    dico["launch"] = Button(root, text="  Go !  ")
    dico["launch"].configure(command=grid_generation)
    dico["launch"].grid(row=5, column=50)

def grid_generation() :
    # if e.get() != "" :
    #     pass #appeler la fonciton de Coco pour faire la grille à partir du fichier
    # # else :
    grid = []
    for i in range(30) :
        grid.append([])
        for j in range(30) :
            if dico[f"b{i}{j}"].cget("bg") == "white" :
                grid[i].append(0)
            else :
                grid[i].append(1)

    dico["e"].destroy()
    dico["launch"].destroy()

    generation_plateau(grid)


def generation_plateau(grid) :
    global dico

    for i in range(30) :
        for j in range(30) :

            if grid[i][j] == 0 :
                color = "white"
            else :
                color = "black"

            dico[f"b{i}{j}"].destroy()
            dico[f"b{i}{j}"] = Label(root, padx=15, pady=5, bg=color, relief=RAISED)
            dico[f"b{i}{j}"].grid(row=i, column=j)
#


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

buttons()

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













































