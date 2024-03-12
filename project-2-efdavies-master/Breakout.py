######################################################################
# Name:Ethan Daves
# Collaborators (if any):
# Section leader's name: OLIVIA
# List of extensions made (if any): I added scores, lives, and winning anf game over messages, I also included a random row and column generation for varying difficulties.
######################################################################

"""
This program (once you have finished it) implements the Breakout game
"""

from pgl import GWindow, GOval, GRect, GLabel
import random

# Constants
GWINDOW_WIDTH = 360                     # Width of the graphics window
GWINDOW_HEIGHT = 600                    # Height of the graphics window
N_ROWS = random.randint(10,10)                    # Number of brick rows
N_COLS = N_ROWS                           # Number of brick columns
BRICK_ASPECT_RATIO = 4 / 1              # Width to height ratio of a brick
BRICK_TO_BALL_RATIO = 3 / 1             # Ratio of brick width to ball size
BRICK_TO_PADDLE_RATIO = 2 / 3           # Ratio of brick to paddle width
BRICK_SEP = 2                           # Separation between bricks (in pixels)
TOP_FRACTION = 0.1                      # Fraction of window above bricks
BOTTOM_FRACTION = 0.05                  # Fraction of window below paddle
N_BALLS = 3                             # Number of balls (lives) in a game
TIME_STEP = 1                          # Time step in milliseconds
INITIAL_Y_VELOCITY = 3.0                # Starting y velocity downwards
MIN_X_VELOCITY = 1.0                    # Minimum random x velocity
MAX_X_VELOCITY = 3.0                    # Maximum random x velocity
# Derived Constants
BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_DIAMETER = BRICK_WIDTH / BRICK_TO_BALL_RATIO
gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
gw.event_count=0
# Function: breakout
def breakout():
    """The main program for the Breakout game."""

    def brick_formation():
        x=1
        y=50
        colors=["red","orange","green","cyan","blue"]

        for i in range (N_ROWS):
            if i >=1:
                x+=BRICK_SEP+(BRICK_WIDTH)
            else:
                x=BRICK_SEP
            for i in range (N_COLS):
                y+=BRICK_SEP+BRICK_HEIGHT
                gw.box=GRect(x,y,BRICK_WIDTH, BRICK_HEIGHT)
                if i%10<=9:
                    gw.box.set_fill_color("blue")
                if i%10<=7:
                    gw.box.set_fill_color("cyan")
                if i%10<=5:
                    gw.box.set_fill_color("green")
                if i%10<=3:
                    gw.box.set_fill_color("orange")
                if i%10<=1:
                    gw.box.set_fill_color("red")
                gw.box.set_filled(True)
                gw.box.set_line_width(1)
                gw.add(gw.box)
            y=50 


    def make_paddle():
        gw.paddle= GRect(GWINDOW_WIDTH/2,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT)
        gw.paddle.set_fill_color("Black")
        gw.paddle.set_filled(True)
        gw.paddle.set_line_width(0)
        gw.add(gw.paddle)
        def movement(e):
            xcord=e.get_x()
            if xcord-PADDLE_WIDTH/2<0:
                xcord=0+PADDLE_WIDTH/2
            if xcord+PADDLE_WIDTH>GWINDOW_WIDTH:    
                xcord=GWINDOW_WIDTH-PADDLE_WIDTH/2
            gw.paddle.set_location(xcord-PADDLE_WIDTH/2,PADDLE_Y)
        gw.add_event_listener("mousemove",movement)

    def click_action(e):
        gw.remove(start)
        gw.ball_is_moving = not gw.ball_is_moving

    def ball():
        gw . vx = random . uniform ( MIN_X_VELOCITY , MAX_X_VELOCITY )
        gw . vy = random . uniform ( MIN_X_VELOCITY , MAX_X_VELOCITY )
        if gw.ball_is_moving==True:
            if random.uniform (0 ,1) < 0.5:
                    gw.vx = - gw.vx
            if random.uniform (0 ,1) < 0.5:
                gw.vy = - gw.vy

    def collide():
        x=gw.sun.get_x()
        y=gw.sun.get_y()
        if gw.ball_is_moving==True:
            if gw.get_element_at(x, y)!=None:
                return gw.get_element_at(x, y)
            if gw.get_element_at(x+BALL_DIAMETER, y)!=None:
                return gw.get_element_at(x+BALL_DIAMETER, y)
            if gw.get_element_at(x, y+BALL_DIAMETER)!=None:
                return gw.get_element_at(x, y+BALL_DIAMETER)
            if gw.get_element_at(x+BALL_DIAMETER, y+BALL_DIAMETER)!=None:
                return gw.get_element_at(x+BALL_DIAMETER, y+BALL_DIAMETER)
            return None

    def lives():
        x=(GWINDOW_WIDTH/12)-(BALL_DIAMETER/2)
        y=(GWINDOW_HEIGHT/20)-(BALL_DIAMETER/2)
        gw.lives_label = GLabel("lives")
        gw.lives_label.set_font("12px 'Press Start 2P'")
        gw.add(gw.lives_label, x, .75*y) 

        gw.life1 = GOval(x, y,BALL_DIAMETER,BALL_DIAMETER)
        gw.life1.set_fill_color("Grey")
        gw.life1.set_filled(True)
        gw.life1.set_line_width(0)
        gw.add(gw.life1)
        x+=(GWINDOW_WIDTH/12)-(BALL_DIAMETER/2)
        gw.life2 = GOval(x, y,BALL_DIAMETER,BALL_DIAMETER)
        gw.life2.set_fill_color("Grey")
        gw.life2.set_filled(True)
        gw.life2.set_line_width(0)
        gw.add(gw.life2)
        x+=(GWINDOW_WIDTH/12)-(BALL_DIAMETER/2)
        gw.life3 = GOval(x, y,BALL_DIAMETER,BALL_DIAMETER)
        gw.life3.set_fill_color("Grey")
        gw.life3.set_filled(True)
        gw.life3.set_line_width(0)
        gw.add(gw.life3)
    
    def step():
       
        points.set_label(str(gw.event_count))
        x = 9*(gw.get_width())  / 12 - points.get_width()  / 2
        y = gw.get_height() / 20 + points.get_ascent() / 2
        points.set_location(x, y)
        if gw.ball_is_moving:
            gw.sun.move(gw.vx, gw.vy)
            if gw.sun.get_y()+BALL_DIAMETER>GWINDOW_HEIGHT:
                gw.ball_is_moving=False
                gw.sun.set_location((GWINDOW_WIDTH/2)-(BALL_DIAMETER/2), (GWINDOW_HEIGHT/2)-(BALL_DIAMETER/2))
                gw.lives=gw.lives-1
                gw.life1.set_fill_color("red")
                if gw.lives<=1:
                    gw.life2.set_fill_color("red")
                if gw.lives==0:
                    gw.life3.set_fill_color("red")
                    gw.remove(gw.sun)
                    msg = GLabel("YOU LOSE")
                    msg.set_font("40px 'Press Start 2P'")
                    x = gw.get_width()  / 2 - msg.get_width()  / 2
                    y = gw.get_height() / 2 + msg.get_ascent() / 2
                    gw.add(msg, x, y)
                    end = GLabel("close & reopen window to play again")
                    end.set_font("10px 'Press Start 2P'")
                    x = gw.get_width()/4.75 - start.get_width()  / 2
                    y = 3*(gw.get_height()) / 4 + start.get_ascent() / 2
                    gw.add(end,x,y)
            if gw.sun.get_x()+BALL_DIAMETER>GWINDOW_WIDTH:
                gw.vx=-gw.vx
            if gw.sun.get_y()<=0:
                gw.vy=-gw.vy
            if gw.sun.get_x()<=0:
                gw.vx=-gw.vx
            object=collide()
            if object==gw.paddle:
                gw.vy=-abs(gw.vy)
            if object!=None and object!=gw.paddle and object!=points and object!=gw.life1 and object!=gw.life2 and object!=gw.life3 and object!=gw.lives_label:
                gw.remove(object)
                gw.event_count += 10
                gw.brick_count=gw.brick_count-1
                gw.vy=-gw.vy
            if gw.brick_count==0 and gw.lives>0:
                gw.remove(points)
                pointsF = GLabel(str(N_ROWS*N_COLS*10))
                pointsF.set_font("30px 'Press Start 2P'")
                x = 9*(gw.get_width())  / 12 - points.get_width()  / 2
                y = gw.get_height() / 20 + points.get_ascent() / 2
                gw.add(pointsF, x, y) 
                gw.event_count += 10
                
                gw.remove(object)
                gw.remove(gw.sun)
                winning_message=["HOORAY!", "WOW!","Congrats!", "WINNER!"]
                msg = GLabel(random.choice(winning_message))
                msg.set_font("40px 'Press Start 2P'")
                x = gw.get_width()  / 2 - msg.get_width()  / 2
                y = gw.get_height() / 2 + msg.get_ascent() / 2
                gw.add(msg, x, y) 
                end = GLabel("close & reopen window to play again")
                end.set_font("10px 'Press Start 2P'")
                x = gw.get_width()/4.75 - start.get_width()  / 2
                y = 3*(gw.get_height()) / 4 + start.get_ascent() / 2

                gw.remove(start) 
                gw.add(end,x,y)
                timer.stop()

    gw.lives= N_BALLS
    gw.brick_count=N_ROWS*N_COLS
    gw.sun = GOval((GWINDOW_WIDTH/2)-(BALL_DIAMETER/2), (GWINDOW_HEIGHT/2)-(BALL_DIAMETER/2),BALL_DIAMETER,BALL_DIAMETER)
    gw.sun.set_fill_color("Black")
    gw.sun.set_filled(True)
    gw.sun.set_line_width(0)
    gw.add(gw.sun)

    start = GLabel("click to start")
    start.set_font("10px 'Press Start 2P'")
    x = gw.get_width()  / 2 - start.get_width()  / 2
    y = 3*(gw.get_height()) / 4 + start.get_ascent() / 2
    gw.add(start, x, y) 



    gw.ball_is_moving=False
    points = GLabel("")
    points.set_font("30px 'Press Start 2P'")
    x = gw.get_width()  / 2 - points.get_width()  / 2
    y = gw.get_height() / 2 + points.get_ascent() / 2
    gw.add(points, x, y) 


    gw.add_event_listener("click", click_action)
    timer = gw.set_interval(step,TIME_STEP)

    lives()
    collide()
    brick_formation()
    ball()
    make_paddle()
    

    # You fill in the rest of this function along with any additional
    # helper and callback functions you need



# Startup code
if __name__ == "__main__":
    breakout()
    

