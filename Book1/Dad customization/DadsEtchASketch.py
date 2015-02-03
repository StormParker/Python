# mtEtchASketch application from Coding Club: Python Basics

from tkinter import *

##### Set variables:
canvas_height = 400
canvas_width = 600
canvas_colour = "yellow"

p1_x = canvas_width/2
p1_y = canvas_height
colour_on = "purple"
colour_off = "black"
p1_colour = colour_on
line_width = 5
line_length = 5

##### Functions

# player controls
def p1_move_N(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length
def p1_move_S(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length
def p1_move_E(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length
def p1_move_W(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length
def erase_all(event):
    canvas.delete(ALL)
def p1_change_pen(event):
    global p1_colour
    if (p1_colour == colour_on):
        p1_colour = colour_off
    else:
        p1_colour = colour_on

##### main:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# bind movement to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("u", erase_all)
window.bind("p", p1_change_pen)

window.mainloop()

