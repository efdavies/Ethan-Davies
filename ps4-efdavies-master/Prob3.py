########################################
# Name: Ethan
# Collaborators: OWEN MECKLEM
# Estimate time spent (hrs): 1
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 15                       # Distance from left of window to origin
SCORE_DY = 15                      # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
gw = GWindow(GW_WIDTH, GW_HEIGHT)
event_count=0
def clicky_box():
    box= GRect((GW_WIDTH/2)-(GW_WIDTH/12), (GW_HEIGHT/2)-(GW_HEIGHT/12),SQUARE_SIZE,SQUARE_SIZE)
    box.set_fill_color("blue")
    box.set_filled(True)
    box.set_line_width(0)
    gw.add(box)

    winner = GLabel("0", SCORE_DX, GW_HEIGHT-SCORE_DY)
    winner.set_font(SCORE_FONT)
    gw.add(winner)
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        x=event.get_x()
        y=event.get_y()
    
        if box.contains(x,y):
            box.set_location(random.randint(0,GW_WIDTH-SQUARE_SIZE),random.randint(0, GW_HEIGHT-SQUARE_SIZE))
            global event_count
            event_count += 1
            winner.set_label(event_count)
            color_string = "#"
            for i in range(6):
                color_string += random.choice("0123456789ABCDEF")
            box.set_fill_color(color_string)
        else:
            event_count=0
            winner.set_label(event_count)
            




    gw.add_event_listener("click", on_mouse_down)

    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function













if __name__ == '__main__':
    clicky_box()