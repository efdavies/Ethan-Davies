#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Ethan
# Who did you work with (if anyone)?: 
# Estimate for time spent on this prob (in hrs)?: 1 hr
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit. Don't forget comments!

import karel


def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    # You can add your code below
    turn_around()
    paint()

def turn_around():
    while left_is_clear():
        turn_left()

def paint():
    while front_is_clear() and left_is_blocked():
        put_beeper()
        move()
        if left_is_clear():
            turn_left()
            move()
            while facing_north():
                move()
                if left_is_clear():
                    turn_left()
                    move()
