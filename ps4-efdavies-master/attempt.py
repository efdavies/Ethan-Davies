from pgl import GWindow, GRect, GOval
import random

WIDTH = 800
HEIGHT = 600
gw=GWindow(WIDTH,HEIGHT)
square=50
gw.dx=0.5
gw.dy=2

def red_box():
    
    def click_action(e):
            if gw.get_element_at(e.get_x(), e.get_y()) == sun: #checking weather I clicked the box
                gw.direction = random.uniform(0, 360) #running the function that changes the direction which the box moves

    def step():
        sun.move_polar(gw.dx,gw.direction)

    
    sun = GOval((WIDTH/2)-(square/2), (HEIGHT/2)-(square/2),square,square) #centering the box
    sun.set_fill_color("blue")
    sun.set_filled(True)
    sun.set_line_width(0)
    gw.add(sun)
    gw.direction = random.uniform(0, 360)
    gw.add_event_listener("click",click_action)
    timer = gw.set_interval(step,5)



if __name__ == "__main__":
    red_box()