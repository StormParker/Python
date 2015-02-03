# This class defines a table that is a 2D rectangle that is a play area.

from tkinter import *

class Table:
    #### constructor
    def __init__(self, window, colour="black", net_colour="white",
                width=600, height=400,
                vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.colour = colour

        # order a canvas to draw on from the tkinter factory:
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()

        # add a net to the canvas using a methos from the tkinter factory:
        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2,
                                    self.height, width=2, fill=net_colour, dash=(15, 23))
        if(horizontal_net):
            self.canvas.create_line(0, self.width/2, self.width/2,
                                    self.height/2, width=2, fill=net_colour, dash=(15, 23))
            
