"""Define the card class."""
class Card:
    """Create one playing card.
    
    Attributes:
        rank (str): the card rank.
        suit (str): the card suit.
    """
    def __init__(self, rank, suit):
        """Sets the card rank and suit.
        
        Args:
            rank (str): the card rank.
            suit (str): the card suit.
        """
        self.rank = rank
        self.suit = suit
    
    def value(self):
        """Return the numeric value of the rank.
        
        Returns:
            int: numeric value of the card.
        """
        values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        return values[self.rank.upper()]
    
    def __str__(self):
        """Return the card as a string.
        
        Returns:
            str: rank and suit together.
        """
        names = {
            "J": "jack",
            "Q": "queen",
            "K": "king",
            "A": "ace",
        }
        
        rank_name = names.get(self.rank.upper(), self.rank)
        return f"{rank_name} of {self.suit}"
    
    