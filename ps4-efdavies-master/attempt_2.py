from pgl import GWindow, GRect, GOval
import random

WIDTH = 800
HEIGHT = 600
gw=GWindow(WIDTH,HEIGHT)
square=50
gw.dx=2
gw.dy=2

def step(event):
    get


timer = gw.set_interval(step,5)
gw.add_event_listener("click", step)