class Player:
    """Create a poker player.
    
    Attributes:
        name (str): the player's name.
        chips (int): amount of chips the player has.
        hand (list): cards in the player's hand.
        folded (bool): whether the player folded
    """
    def __init__(self, name, chips=100):
        """Set the player's starting values.

        Args:
           name (str): player name.
           chips (int): starting chip amount
        """
        self.name = name
        self.chips = chips
        self.hand = []
        self.folded = False