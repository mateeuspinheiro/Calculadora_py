# import tkinter
from tkinter import *
from tkinter import ttk

colordsp = "#798686" #display
colorbg = "#e6f2ff" #bg
colorbody = "#798686" #body

window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=colorbg)

#frames
frame_display = Frame(window, width=235, height=70, bg=colordsp)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=258, bg=colorbg)
frame_body.grid(row=1, column=0)

#buttons


window.mainloop()
