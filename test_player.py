from card import Card
from player import Player

def test_receive_card():
    player = Player("Mo")
    player.receive_card(Card("Q", "diamonds"))
    assert len(player.hand) == 1

def test_bet():
    player = Player("Mo", 100)
    assert player.bet(25) == 25
    assert player.chips == 75