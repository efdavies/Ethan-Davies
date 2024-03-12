# File: Card.py

"""This file defines the Card class."""

# Constants

RANK_SYMBOLS = [ "A","2","3","4","5","6","7","8","9","10","J","Q","K" ]
SUIT_SYMBOLS = [ "\u2663", "\u2666", "\u2665", "\u2660" ] 

# Client notes: Card class
# ------------------------
# The Card class defines a standard playing card object which has
# attributes corresponding to both rank and suit.  This module also
# exports several class variables for convenience corresponding to the
# numeric suit ranks, which can be accessed, for example, as Card.CLUBS
# or Card.HEARTS.

class Card:
    """This class defines a standard playing card object."""

    # Constants
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

    def __init__(self, rank, suit):
        """
        Creates a new card object.

        Inputs:
            rank (int): value between 1 and 13 corresponding to Ace -- King
            suit (int): a value between 0 and 3 corresponding to suit
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """Returns a string version of a Card using human-readable symbols."""
        return RANK_SYMBOLS[self.rank - 1] + SUIT_SYMBOLS[self.suit]

    def get_rank(self):
        """Returns the numeric rank of a card, between 1 and 13, inclusive."""
        return self.rank

    def get_suit(self):
        """Returns the numeric suit of a card, between 0 and 3, inclusive."""
        return self.suit

def test_card_class():
    """Performs a unit test of the Card class."""
    for suit in range(0, 4):
        suit_symbol = SUIT_SYMBOLS[suit]
        for rank in range(1, 14):
            rank_symbol = RANK_SYMBOLS[rank - 1]
            card = Card(rank, suit)
            assert card.get_rank() == rank
            assert card.get_suit() == suit
            assert str(card) == rank_symbol + suit_symbol

if __name__ == "__main__":
    test_card_class()
