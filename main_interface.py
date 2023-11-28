# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

# def add_point():
#     # Exemple pour ajouter un point sur la carte
#     x, y = float(entry_x.get()), float(entry_y.get())
#     ax.plot(x, y, 'ro')  # 'ro' signifie "red circle"
#     canvas.draw()

# # Création de la fenêtre Tkinter
# root = tk.Tk()
# root.title("Carte 2D Interactive")

# # Création d'une figure matplotlib
# fig = Figure()
# ax = fig.add_subplot(111)
# ax.set_xlim([0, 100])  # Définir les limites de l'axe
# ax.set_ylim([0, 100])  # Définir les limites de l'axe

# # Intégration de matplotlib dans Tkinter
# canvas = FigureCanvasTkAgg(fig, master=root)
# widget = canvas.get_tk_widget()
# widget.pack()

# # Champ de saisie et bouton pour ajouter un point
# entry_x = tk.Entry(root)
# entry_x.pack()
# entry_y = tk.Entry(root)
# entry_y.pack()
# button = tk.Button(root, text="Ajouter un point", command=add_point)
# button.pack()

# root.mainloop()

# ======================================================================================================================

# import tkinter as tk

# def create_grid(event=None):
#     w = canvas.winfo_width() # Obtenir la largeur actuelle du canvas
#     h = canvas.winfo_height() # Obtenir la hauteur actuelle du canvas
#     canvas.delete('grid_line') # Supprimer les anciennes lignes de grille

#     # Créer de nouvelles lignes de grille
#     for i in range(0, w, 20): # lignes verticales tous les 20 pixels
#         canvas.create_line([(i, 0), (i, h)], tag='grid_line')

#     for i in range(0, h, 20): # lignes horizontales tous les 20 pixels
#         canvas.create_line([(0, i), (w, i)], tag='grid_line')

# root = tk.Tk()
# root.geometry('400x400') # Taille initiale de la fenêtre

# canvas = tk.Canvas(root, bg='white')
# canvas.pack(fill=tk.BOTH, expand=True)

# canvas.bind('<Configure>', create_grid)

# root.mainloop()

#  ======================================================================================================================

# import tkinter as tk

# def update_color(square_id, color):
#     canvas.itemconfig(square_id, fill=color)

# def some_program_logic():
#     # Cette fonction représente la logique de votre programme
#     # qui détermine quand et comment changer la couleur des carrés
#     # Par exemple, changeons la couleur du premier carré en rouge
#     update_color(squares[0], 'red')

# root = tk.Tk()

# canvas = tk.Canvas(root)
# canvas.pack(fill=tk.BOTH, expand=True)

# # Dessiner des carrés
# squares = []
# for i in range(5):
#     square = canvas.create_rectangle(50 * i, 50 * i, 50 * i + 50, 50 * i + 50, fill='blue')
#     squares.append(square)

# # Appel de la fonction de logique du programme
# some_program_logic()

# root.mainloop()

# ======================================================================================================================

import tkinter as tk

def on_hover(event, square_id):
    # Récupérer les caractéristiques du carré
    coords = canvas.coords(square_id)
    color = canvas.itemcget(square_id, 'fill')
    info_label.config(text=f"Caractéristiques: Coordonnées {coords}, Couleur {color}")

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

info_label = tk.Label(root, text="Passez la souris sur une case")
info_label.pack()

squares = []
for i in range(5):
    square = canvas.create_rectangle(50 * i, 50, 50 * i + 50, 100, fill='blue', tags="square")
    squares.append(square)

    # Lier l'événement de survol pour chaque carré
    canvas.tag_bind(square, "<Enter>", lambda e, square_id=square: on_hover(e, square_id))

root.mainloop()
