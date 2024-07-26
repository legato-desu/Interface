# Select list

from tkinter import *
"""
Create a RadioButton list that displays the option that has been selected and contains 
a reset button to leave everything as it was at the beginning.

At first there does not have to be an option selected.
"""
def select():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
root.title("Legato")

Radiobutton(root, text="Anime", variable=opcion, value="Anime", command=select).pack(anchor=W)
Radiobutton(root, text="Cosplay", variable=opcion, value="Cosplay", command=select).pack(anchor=W)
Radiobutton(root, text="Manga", variable=opcion, value="Manga", command=select).pack(anchor=W)
Radiobutton(root, text="Japon", variable=opcion, value="Japon", command=select).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Limpiar", command=reset, fg="blue").pack()

root.mainloop()