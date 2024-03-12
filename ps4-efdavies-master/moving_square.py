from pgl import GWindow, GRect, GOval
import random

WIDTH = 800
HEIGHT = 600
gw=GWindow(WIDTH,HEIGHT)
square=50
gw.dx=2
gw.dy=2
def step():
    sun.move(gw.dx, gw.dy)
    if sun.get_y()+square>HEIGHT:
        gw.dy=-gw.dy
    if sun.get_x()+square>WIDTH:
        gw.dx=-gw.dx
    if sun.get_y()<=0:
        gw.dy=-gw.dy
    if sun.get_x()<=0:
        gw.dx=-gw.dx

sun = GOval((WIDTH/2)-(square/2), (HEIGHT/2)-(square/2),square,square)
sun.set_fill_color("blue")
sun.set_filled(True)
sun.set_line_width(0)
gw.add(sun)
timer = gw.set_interval(step,5)