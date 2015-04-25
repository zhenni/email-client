#!/usr/bin/python

import Tkinter
from Tkinter import *

root = Tkinter.Tk()
root.title("Mail Client Demo")
scnWidth,scnHeight = root.maxsize()
WIDTH = 600
HEIGHT = 600
FONT = 'Helvetica'
pos = '%dx%d+%d+%d'%(WIDTH, HEIGHT, (scnWidth-WIDTH)/2, (scnHeight-HEIGHT)/2)
root.geometry(pos)

#Title
label = Tkinter.Label(root,text='Mail Client Demo',font=FONT+' -30 bold')
label.pack()

#Frame
frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='4', font=(FONT, 15)).pack(side=TOP)
Label(frm_L, text='3', font=(FONT, 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
def printhello():
	var.set("welcome "+var.get()+" !")

frm_R = Frame(frm)
#t = Text(frm_R)
#t.pack(side=TOP)

var = StringVar()
e = Entry(frm_R, textvariable = var)
var.set("Entry your email address")
e.pack()
Button(frm_R, text="press", command = printhello).pack(side=BOTTOM)
frm_R.pack(side=RIGHT)

frm.pack()


root.mainloop()

