import karel
# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a function below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    while no_beepers_present():
        layer_one()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def layer_one():
    while facing_east() and front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
        else:
            turn_left()
            if front_is_clear():
                    move()
                    turn_left()
    layer_two()

def layer_two():
    while facing_west() and front_is_clear():
        if no_beepers_present():
            move()
            put_beeper()
        else:
            if no_beepers_present():
                put_beeper()
            move()
    for i in range(1):
        if front_is_blocked():
            turn_right()
            if front_is_clear():
                move()
                turn_right()
    
    
    
