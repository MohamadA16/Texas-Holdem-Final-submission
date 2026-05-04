from card import Card

def test_card_value_ace():
    assert Card("A", "spades").value() == 14

def test_card_value_tem():
    assert Card("10", "heart").value() == 10
    
def test_card_value_string():
    assert str(Card("K", "clubs")) == "king of clubs"