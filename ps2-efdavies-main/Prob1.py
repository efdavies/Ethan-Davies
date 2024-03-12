#====================================================
# Filename: Prob1.py
# 
# Your name: Ethan davies
# Who did you work with (if anyone)?: no
# Estimate for time spent (in hrs)?: 1.3
#====================================================

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
        if beepers_present():
            go_to_next_layerO()
        else:
            go_to_next_layerE()
        layer_two()
        if right_is_clear():
            go_to_next_layer2()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_next_layerO(): #for odd dimensions e.g. 5x3
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        move()

def go_to_next_layerE(): #for even dimentions e.g. 8x8
    turn_left()
    if front_is_clear():
        move()
        turn_left()

def go_to_next_layer2(): 
    turn_right()
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
        if no_beepers_present():
            put_beeper()
            move()
            if front_is_clear():
                move()





        
    
   

# Remember to define any more helper functions you want down here


