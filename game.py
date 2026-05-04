import sys
import argparse
from deck import Deck
from player import Player
from hand_evaluator import best_hand, hand_name

class Game:
    """Run one simple round of Texas Hold'em."""

    def __init__(self, player1_name, player2_name):
        """Create a game with two players.

        Args:
            player1_name (str): name of player 1.
            player2_name (str): name of player 2.
        """
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
    