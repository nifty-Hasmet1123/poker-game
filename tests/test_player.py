from poker.card import Card
from poker.hand import Hand
from poker.player import Player
from unittest.mock import MagicMock
import unittest

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        
        player = Player(name = "Maxi", hand = hand)
        self.assertEqual(player.name, "Maxi")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        
        # this should be included, this ensures that the 
        # return value of the best_hand instance in the player.py
        # is actually returning the best_rank() method in the hand.py
        mock_hand.best_rank.return_value = "Straight Flush"

        player = Player(name = "Maxi", hand = mock_hand)
        
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name = "Sharon", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_player_is_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (
            0, 
            "Royal Flush",
            []
        )

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (
            0,
            "Pair",
            []
        )

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )