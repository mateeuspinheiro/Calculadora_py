# import tkinter
from tkinter import *
from tkinter import ttk

colordsp = "#798686" #display
colorbg = "#e6f2ff" #bg
colorbody = "#798686" #body
colorgray = "#b6b4af" #gray
colorwhite = "#ffffff" #white
colororange = "#ffd480" #orange

window = Tk()
window.title("Calculadora")
window.geometry("235x339")
window.config(bg=colorbg)

#frames
frame_display = Frame(window, width=235, height=70, bg=colordsp)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268, bg=colorbg)
frame_body.grid(row=1, column=0)

#buttons
b1 = Button(frame_body, text="C", width=11, height=2, bg=colorgray, font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)
b2 = Button(frame_body, text="%", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)
b3 = Button(frame_body, text="/", width=5, height=2, bg=colororange, fg=colorwhite,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)
b4 = Button(frame_body, text="7", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=55)
b5 = Button(frame_body, text="8", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b5.place(x=60,y=55)
b6 = Button(frame_body, text="9", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=55)
b7 = Button(frame_body, text="*", width=5, height=2, bg=colororange, fg=colorwhite,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=55)
b8 = Button(frame_body, text="4", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=110)
b9 = Button(frame_body, text="5", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b9.place(x=60,y=110)
b10 = Button(frame_body, text="6", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=110)
b11 = Button(frame_body, text="-", width=5, height=2, bg=colororange, fg=colorwhite,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=110)
b12 = Button(frame_body, text="1", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=165)
b13 = Button(frame_body, text="2", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b13.place(x=60,y=165)
b14 = Button(frame_body, text="3", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=165)
b15 = Button(frame_body, text="+", width=5, height=2, bg=colororange, fg=colorwhite,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=165)
b1 = Button(frame_body, text="0", width=11, height=2, bg=colorgray, font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=220)
b2 = Button(frame_body, text=".", width=5, height=2, bg=colorgray,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=220)
b3 = Button(frame_body, text="=", width=5, height=2, bg=colororange, fg=colorwhite,font=('Arial 13 italic'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=220)

window.mainloop()
