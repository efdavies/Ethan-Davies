
import karel

def main():
    climb_stairs()
   decend()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def climb_stairs():
    while facing_east():
        while front_is_clear():
            move()
        turn_left()
        move()
        turn_right()

        
def 


