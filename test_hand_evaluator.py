from card import Card
from hand_evaluator import evaluate_five_card_hand, hand_name, best_hand

def test_one_pair_case():
    cards = [
        Card("A", "spades"),
        Card("A", "hearts"),
        Card("7", "diamonds"),
        Card("4", "clubs"),
        Card("2", "spades")
    ]
    assert evaluate_five_card_hand(cards)[0] == 1
    