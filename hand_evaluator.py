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
    
    if len(unique_values) == 5:
        if unique_values[-1] - unique_values[0] == 4:
            is_straight = True
        elif unique_values == [2, 3, 4, 5, 14]:
            is_straight = True
            values = [5, 4, 3, 2, 1]

    if is_straight and is_flush:
        return (8, values)
    if count_values == [4, 1]:
        return (7, values)
    if count_values == [3, 2]:
        return (6, values)
    if is_flush:
        return (5, values)
    if is_straight:
        return (4, values)
    if count_values == [3, 1, 1]:
        return (3, values)
    if count_values == [2, 2, 1]:
        return (2, values)
    if count_values == [2, 1, 1, 1]:
        return (1, values)
    return (0, values)

def best_hand(seven_cards):
    """Find the best 5-card hand from 7 cards.

    Args:
        seven_cards (list): a list of 7 Card objects.

    Returns:
        tuple: best score and best cards.
    """
    best_score = None
    best_cards = None

    for combo in combinations(seven_cards, 5):
        score = evaluate_five_card_hand(combo)
        if best_score is None or score > best_score:
            best_score = score
            best_cards = combo

    return best_score, best_cards

def hand_name(score):
    """Convert a score into a hand name.

    Args:
        score (tuple): the score returned by the evaluator.

    Returns:
        str: name of the poker hand.
    """
    names = {
        8: "Straight Flush",
        7: "Four of a Kind",
        6: "Full House",
        5: "Flush",
        4: "Straight",
        3: "Three of a Kind",
        2: "Two Pair",
        1: "One Pair",
        0: "High Card",
    }
    return names[score[0]]