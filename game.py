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
    
    def setup_round(self):
        """Set up the deck and reset player hands."""
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.player1.clear_hand()
        self.player2.clear_hand()
    
    def deal_hole_cards(self):
        """Deal two cards to each player."""
        for _ in range(2):
            self.player1.receive_card(self.deck.deal_card())
            self.player2.receive_card(self.deck.deal_card())

    def deal_flop(self):
        """Deal the first three community cards."""
        for _ in range(3):
            self.community_cards.append(self.deck.deal_card())
            
    def deal_turn(self):
        """Deal the fourth community card."""
        self.community_cards.append(self.deck.deal_card())

    def deal_river(self):
        """Deal the fifth community card."""
        self.community_cards.append(self.deck.deal_card())

    def betting_round(self):
        """Run one simple betting round."""
        for player in [self.player1, self.player2]:
            if player.folded:
                continue

            print(f"\\n{player.name}, you have {player.chips} chips.")
            action = input("Choose: check, bet, or fold: ").strip().lower()
    
            if action == "fold":
                player.fold()
            elif action == "bet":
                amount = int(input("Enter bet amount: "))
                self.pot += player.bet(amount)
    
    def determine_winner(self):
        """Figure out who won the round.

        Returns:
            Player or None: winner or None if it is a tie.
        """
        if self.player1.folded:
            return self.player2
        if self.player2.folded:
            return self.player1

        score1, _ = best_hand(self.player1.hand + self.community_cards)
        score2, _ = best_hand(self.player2.hand + self.community_cards)

        if score1 > score2:
            return self.player1
        if score2 > score1:
            return self.player2
        return None
    
    
    def show_results(self):
        """Print the final results."""
        print("\\nCommunity Cards:", " | ".join(str(card) for card in self.community_cards))
        print(f"{self.player1.name} hand: {' | '.join(str(card) for card in self.player1.hand)}")
        print(f"{self.player2.name} hand: {' | '.join(str(card) for card in self.player2.hand)}")

        score1, _ = best_hand(self.player1.hand + self.community_cards)
        score2, _ = best_hand(self.player2.hand + self.community_cards)

        print(f"{self.player1.name} best hand: {hand_name(score1)}")
        print(f"{self.player2.name} best hand: {hand_name(score2)}")

        winner = self.determine_winner()
        if winner is None:
            print("Tie game.")
        else:
            winner.chips += self.pot
            print(f"Winner: {winner.name}")
            print(f"{winner.name} wins {self.pot} chips.")
    
def main(player1_name, player2_name):
     """Start and play one round of the game."""
     game = Game(player1_name, player2_name)
     game.setup_round()
     game.deal_hole_cards()

     print(f"{player1_name} cards: {' | '.join(str(card) for card in game.player1.hand)}")
     print(f"{player2_name} cards: {' | '.join(str(card) for card in game.player2.hand)}")

     input("Press Enter for the flop...")
     game.deal_flop()
     print("Flop:", " | ".join(str(card) for card in game.community_cards))
     game.betting_round()

     input("Press Enter for the turn...")
     game.deal_turn()
     print("Turn:", " | ".join(str(card) for card in game.community_cards))
     game.betting_round()

     input("Press Enter for the river...")
     game.deal_river()
     print("River:", " | ".join(str(card) for card in game.community_cards))
     game.show_results()
     
def parse_args(args_list):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('player1_name', type=str, help="Please enter Player 1's name")
    parser.add_argument('player2_name', type=str, help="Please enter Player 2's name")
    args = parser.parse_args(args_list)
    return args
    
if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    main(arguments.player1_name, arguments.player2_name)

