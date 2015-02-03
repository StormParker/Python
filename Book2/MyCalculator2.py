# myCalculator_expt1.py

from tkinter import *
from decimal import *

# key press function:
def click(key):
    display.insert(END, key)

##### main:
window = Tk()
window.title("MyCalculator")

# create top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry widget for an editable display
display = Entry(window, width=45, bg='light green')
display.grid()

# create num_pad_frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# create num_pad buttons:
def click1():
    display.insert(END, "1")
Button(window, text="1", width=5, command=click1).grid(row=1,column=0)

##### Run mainloop
window.mainloop()
