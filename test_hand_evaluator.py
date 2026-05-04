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

def test_flush_case():
    cards = [
        Card("2", "hearts"),
        Card("5", "hearts"),
        Card("8", "hearts"),
        Card("J", "hearts"),
        Card("K", "hearts")
    ]
    assert hand_name(evaluate_five_card_hand(cards)) == "Flush"

def test_best_hand_returns_score():
    cards = [
        Card("A", "spades"),
        Card("A", "hearts"),
        Card("K", "diamonds"),
        Card("Q", "clubs"),
        Card("J", "spades"),
        Card("2", "clubs"),
        Card("3", "diamonds")
    ]
    score, best_cards = best_hand(cards)
    assert score is not None
    assert len(best_cards) == 5
