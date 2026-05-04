"""Define the deck class."""

import random
from card import Card

class Deck:
    """Create and manage a deck of cards."""
    
    def __init__(self):
        """Create a standard 52 card deck."""
        ranks = [
            "2", "3", "4", "5", "6", "7", "8","9", "10", "J", "Q", "K", "A"
        ]
        suits = ["spades", "hearts", "diamond", "clubs"]
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        
    def shuffle(self):
        """Shuffle the deck.
        
        side effects:
            Changes the order of the cards in the deck.
        """
        random.shuffle(self.cards)
        
    def deal_card(self):
        """Deal one card from the deck.
        
        Returns:
            Card: the dealt card.
        """
        return self.cards.pop()