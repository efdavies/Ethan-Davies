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
    while front_is_clear() and left_is_blocked() and right_is_clear():
        put_beeper()
        move()
        if left_is_clear():
            turn_left()
            move()
            while facing_north():
                if left_is_clear():
                    turn_left()
                    move()
                else: 
                    move()
