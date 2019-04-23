import keyboard
import os
import mouse
import threading
import time
from adjacent import is_adjacent, adjacent_rate
from tkinter import *
from queue import Queue
from predict import predict
from functools import partial
import numpy as np


win = Tk()
win.update()
print("x: ", str(win.winfo_x()))
print("y: ", str(win.winfo_y()))
mouse_position = mouse.get_position()
print("mouse: ", mouse_position[0], mouse_position[1])
position = "+"+str(mouse_position[0])+"+"+str(mouse_position[1])
win.geometry(position)
win.mainloop()