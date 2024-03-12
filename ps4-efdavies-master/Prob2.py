########################################
# Name:
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE =15


def draw_rect(x,y,gw):
    rect = GRect(x+BRICK_WIDTH/2, y+BRICK_HEIGHT/2, BRICK_WIDTH, BRICK_HEIGHT)
    rect.set_fill_color("orange")
    rect.set_filled(True)
    rect.set_line_width(1)
    gw.add(rect)

def draw_pyramid():

    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    x=(WIDTH/2)-(BRICK_WIDTH)
    y=(HEIGHT/2)-(BRICK_HEIGHT/2)
    p_height=(BRICKS_IN_BASE * BRICK_HEIGHT)/2

    gw = GWindow(WIDTH, HEIGHT)

    for i in range(BRICKS_IN_BASE):
        k=y-(p_height)+i*BRICK_HEIGHT
        for j in range(i+1):
            draw_rect(x-i*BRICK_WIDTH/2+j*BRICK_WIDTH,k,gw)


if __name__ == '__main__':
    draw_pyramid()
