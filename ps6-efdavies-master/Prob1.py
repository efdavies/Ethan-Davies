##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

"""Compose a suitable docstring comment for the module."""

from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self,n):
        cards_drawn=[]
        for i in range(n):
            cards_drawn.append(self.cards.pop())
        return cards_drawn

    def get_deck(self):
        return(self.cards.copy())

    def __str__(self):
        return str(self.cards)
        



    """Implement the Deck class, including all required methods. """

def test_deck_class():
    D= Deck()
    assert D != D.shuffle()
    assert len(D.get_deck()) > 52 - len(D.draw_cards(3))
    print("initial deck",D)
    D.shuffle()
    print("shuffled cards",D)
    print("three random cards",D.draw_cards(3))
    print("printing D", D)
    print("length of the deck", len(D.get_deck()))
    """Implement a unit test of the Deck class."""

if __name__ == "__main__":
    test_deck_class()
