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
        