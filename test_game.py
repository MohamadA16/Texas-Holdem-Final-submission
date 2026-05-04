from game import Game

def test_deal_hole_cards():
    game = Game("A", "B")
    game.setup_round()
    game.deal_hole_cards()
    assert len(game.player1.hand) == 2
    assert len(game.player2.hand) == 2

