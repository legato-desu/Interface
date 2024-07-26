# Colombia window

import tkinter
"""
Create a window with the colors of Colombia and their meaning
"""

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Riquesa", bg="yellow", fg="black")
label1.pack(ipadx=50, ipady=50, fill="both")

label2 = tkinter.Label(window, text="Abundancia", bg="blue", fg="black")
label2.pack(ipadx=50, ipady=50, fill="both")

label3 = tkinter.Label(window, text="Sangre ", bg="red", fg="black")
label3.pack(ipadx=50, ipady=50, fill="both")

window.mainloop()