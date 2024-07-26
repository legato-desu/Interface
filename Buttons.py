# Buttons

import tkinter
"""
Create a window to display button events
"""
window = tkinter.Tk()
def greet(event):
    print("Han dado clic aqui")
def greetDobleClic(event):
    print("has dado doble clic")
def exit(event):
    window.quit()

boton = tkinter.Button(window, text="Clic aqui")
boton.pack()
boton.bind("<Button-1>",greet)
boton.bind("<Double-1>",greetDobleClic)



botonexit = tkinter.Button(window, text="Exit")
botonexit.pack()
botonexit.bind("<Button-1>",exit)
window.quit()


window.mainloop()