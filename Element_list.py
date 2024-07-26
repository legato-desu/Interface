# Element list

from tkinter import *
"""
create a simple interface which must contain a list of selectable elements, 
it must also have a label with the text you want.
"""
master = Tk()
master.title("Marcas")
master.geometry("200x210")
elemento = StringVar()
listbox = Listbox(master)
for item in ["Yamaha", "Suzuki", "kawasaki", "Bmw"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Marcas Motocicletas")
label.pack()
master.mainloop()