# This class defines a Table that is 2D rectangle that is a play area.

from tkinter import *

class Table:
        #### constructor
        def __init__(self, window, colour="black", net_colour="green",
                     width=600, height=400,
                     vertical_net=False, horizontal_net=False):
                self.width = width
                self.height = height
                self.colour = colour
