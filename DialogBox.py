"""import tkinter as t
from tkinter import *

root = t.Tk(className=" Chess Game")
frame = t.Frame(root)
frame.pack()

button_one = t.Button(frame, text="Player vs Player", bg="Blue", fg="White",  padx=10, pady=10)
button_one.pack()
button_two = t.Button(frame, text="Player vs Computer", padx=10, pady=10)
button_two.pack()

root.geometry("450x350")

root.mainloop()

import tkinter as tk

root = tk.Tk()
for text in enumerate((
        "Hello", "short", "All the buttons are not the same size",
        "Options", "Test2", "ABC", "This button is so much larger")):
    button = tk.Button(root, text=text)
    button.grid(row=row, column=0, sticky="ew")


root.mainloop()
"""
"""
import tkinter as t
from tkinter import *

#def ask_multiple_choice_question(prompt, options):
root = t.Tk(className=" Chess Game")
frame = t.Frame(root)
frame.pack()

"""

"""   
    if prompt:
        #Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0: return None
    return options[v.get()]

result = ask_multiple_choice_question(
    "What is your favorite color?",
    [
        "Blue!",
        "No -- Yellow!",
        "Aaaaargh!"
    ]
)

print("User's response was: {}".format(repr(result)))
"""
"""
from tkinter import Tk, Label, Button, Radiobutton, IntVar
#    ^ Use capital T here if using Python 2.7

def ask_multiple_choice_question(prompt, options):
    root = Tk()
    if prompt:
        Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0: return None
    return options[v.get()]

result = ask_multiple_choice_question(
    "What is your favorite color?",
    [
        "Blue!",
        "No -- Yellow!",
        "Aaaaargh!"
    ]
)

print("User's response was: {}".format(repr(result)))
"""
"""
import tkinter as t
from tkinter import *

root = t.Tk(className=" Chess Game")
frame = t.Frame(root)
frame.pack()

button_one = t.Button(frame, text="Player vs Player", padx=10, pady=10)
button_one.pack()
button_two = t.Button(frame, text="Player vs Computer", padx=10, pady=10)
button_two.pack()

root.geometry("450x350")

root.mainloop()


"""
from ChessMain import *
from ChessEngine import *
from ChessAI import *


import tkinter as t
from tkinter import *

root = t.Tk(className=" Chess Game")
frame = t.Frame(root)
frame.pack()

def PvsP():
    playerOne = True
    playerTwo = True

button_one = t.Button(frame, text="Player vs Player", command=PvsP, padx=10, pady=10)
button_one['command'] = PvsP
button_one.pack(padx=10, pady=10)

def PvsC():
    playerOne = True
    PlayerTwo = False
button_two = t.Button(frame, text="Player vs Computer", command= PvsC,padx=10, pady=10)
button_two['command'] = PvsC
button_two.pack()

#dialog.setCanceledOnTouchOutside(false);

root.geometry("250x150")
root.mainloop()