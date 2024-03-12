########################################
# Name: Ethan
# Collaborators (if any): 
# Estimated time spent (hr): 3
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import CAPITAL_ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random

def wordle():
    """ The main function to play the Wordle game. """
    window=WordleGWindow() 
    hidden = CAPITAL_ENGLISH_WORDS 
    while len(hidden)!=5: #makes a random 5 letter word each time
        hidden=random.choice(CAPITAL_ENGLISH_WORDS)
        print(hidden)
    guess = ""

    def enter_action():
        nonlocal guess #non local gives permission to change your guess each time you press enter because guess is outside of the def of enter initially
        guess=""
        for i in range(N_COLS): 
            guess+=window.get_square_letter(window.get_current_row(),i)
        print(guess)
        if is_english_word(guess) and len(guess)==5: #checks if the word you input is an actual word, then colors it and checks if its a winner
            color_letters()
            check_winner()

        else: # tells us its not a word if the word doesnt exist and is not 5 letters
            window.show_message("this is not a word, try again")

    

    def color_letters():
        unmatched = hidden
        for col in range(N_COLS):
            if guess[col] == hidden[col]: #if the letter is in the string check if it is in the same spot as the hiden then turns it green along with the key
                window.set_square_color(window.get_current_row(), col, CORRECT_COLOR)
                window.set_key_color(guess[col], CORRECT_COLOR )
                unmatched = unmatched.replace(guess[col], "", 1)
            if guess[col] != hidden[col]: #Checking if the letter is in the word, and coloring it grey if its not
                window.set_square_color(window.get_current_row(), col, MISSING_COLOR)
                window.set_key_color(guess[col], MISSING_COLOR)
        for col1 in range(N_COLS):
            window.set_square_letter(window.get_current_row(), col1, guess[col1])
            if  guess[col1] in unmatched and window.get_square_color(window.get_current_row(),col1)!=CORRECT_COLOR: #to check if the letter is in the string but not in the right spot, turns yellow
                window.set_square_color(window.get_current_row(), col1, PRESENT_COLOR)
                window.set_key_color(guess[col1], PRESENT_COLOR )
                unmatched = unmatched.replace(guess[col1], "", 1)

        
    def check_winner(): 
        # winning messages
        message_list=["Good job! Now try to find the rest", "Nice try", "Keep going!"]
        winning_message=["YOU WIN!","WOW! GREAT JOB!", "WOWOWOWOWOWOWOWOWOWOWOWOWOWOW", "YOU'RE A SMART COOKIE!"]
        #displaying messages in window while playing
        if guess==hidden:
            window.show_message(random.choice(winning_message)) #cannot enter anymore after you get the winning message
        elif window.get_current_row() !=6: #as long as we are not on the 6th row it will show an encouragng message
            window.show_message(random.choice(message_list))
            next_row = window.get_current_row() + 1
            window.set_current_row(next_row)
        if window.get_current_row() == 6 and guess !=hidden: #if the player has run out of guesses
                window.show_message("Better luck next time! The word was " + hidden)
        


    window.add_enter_listener(enter_action)

    






""" What should happen when the RETURN or ENTER key is pressed. """








# Startup boilerplate
if __name__ == "__main__":
    wordle()
