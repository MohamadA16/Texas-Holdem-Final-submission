from collections import Counter
from itertools import combinations

def evaluate_five_card_hand(cards):
    """Give a score to five cards.

    Args:
        cards (list): a list of 5 Card objects.

    Returns:
        tuple: hand rank and card values.
    """
    values = sorted([card.value() for card in cards], reverse=True)
    suits = [card.suit for card in cards]
    counts = Counter(values)
    count_values = sorted(counts.values(), reverse=True)
    unique_values = sorted(set(values))

    is_flush = len(set(suits)) == 1
    is_straight = False