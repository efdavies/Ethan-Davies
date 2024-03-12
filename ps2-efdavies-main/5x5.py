import karel
# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a function below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    if front_is_blocked():
        turn_left()
        layer_one()
    else:
     while front_is_clear():
        layer_one()
        go_to_next_layer1()
        layer_two()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_next_layer1():
    turn_left()
    move()
    turn_left()
def go_to_next_layer2():
    move()
    turn_right()

def layer_one():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            if no_beepers_present():
                put_beeper()

def layer_two():
    while front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()
            if front_is_clear():
                move()
                if front_is_blocked():
                    turn_right()