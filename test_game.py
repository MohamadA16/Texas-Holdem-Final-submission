from game import Game

def test_deal_hole_cards():
    game = Game("A", "B")
    game.setup_round()
    game.deal_hole_cards()
    assert len(game.player1.hand) == 2
    assert len(game.player2.hand) == 2

def test_flop_turn_river_counts():
    game = Game("A", "B")
    game.setup_round()
    game.deal_flop()
    assert len(game.community_cards) == 3
    game.deal_turn()
    assert len(game.community_cards) == 4
    game.deal_river()
    assert len(game.community_cards) == 5