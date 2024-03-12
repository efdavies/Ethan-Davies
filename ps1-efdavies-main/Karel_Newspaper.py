#========================================================
# Filename: Karel_Newspaper.py
# 
# Your name: Ethan
# Who did you work with (if anyone)?: no one
# Estimate for time spent on this problem (in hrs)?: 0.08
#========================================================

# I've just laid out a basic starting function below. 
# While this problem is fairly simple, you should still practice
# the good habit of writing helper functions to decompose the problem
# into smaller pieces. I have provided you with a template for the
# main function and then 3 helping functions as outlined in the PDF

import karel


def main():

    """ Function to cause Karel to retrieve the newspaper. """
    # You can add your sequence of commands below here!
    # Remember you can use the defined helper functions!
    move_to_newspaper()
    pick_up_paper()
    return_to_start()

def move_to_newspaper():
    """ Helping function to move Karel to the newspaper location. """
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()

def pick_up_paper():
    """ Helping function to have Karel pick up the newspaper. """
    # Yes, this will probably be VERY simple and short
    pick_beeper()


def return_to_start():
    """ Helping function to move Karel back to its starting position. """
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    move()
