from deck import Deck
def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52
    
def test_deal_card_removes_one_card():
    deck = Deck()
    deck.deal_card()
    assert len(deck.cards) == 51