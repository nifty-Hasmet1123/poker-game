from poker.card import Card
from poker.deck import Deck
from poker.player import Player
from poker.game_round import GameRound
from unittest.mock import MagicMock, call # call is used to mimic the callable function
import unittest


class GameRoundTest(unittest.TestCase):
    def setUp(self): # when using this you need to make sure the variables are in self object.
        self.first_two_cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Clubs")
        ]

        self.next_two_cards = [
            Card(rank = "8", suit = "Spades"),
            Card(rank = "King", suit = "Diamonds")
        ]

        self.flop_cards = [
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "10", suit = "Spades")
        ]

        self.turn_card = [
            Card(rank = "9", suit = "Hearts")
        ]

        self.river_card = [
            Card(rank = "Queen", suit = "Clubs")
        ]
    def test_store_deck_and_players(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]

        game_round = GameRound(deck = mock_deck, players = mock_players)

        self.assertEqual(
            game_round.deck,
            mock_deck
        )

        self.assertEqual(
            game_round.players,
            mock_players
        )

    def test_play_game_shuffles_deck(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]

        game_round = GameRound(deck = mock_deck, players = mock_players)

        game_round.play()
        mock_deck.shuffle_cards.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock() 
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards, 
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        players = [
            mock_player1, mock_player2
        ]

        game_round = GameRound(deck = mock_deck, players = players)
        
        game_round.play()

        # test if remove_cards is called on two player.
        # the argument of 2 represents the number of cards to be removed.
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2) 
        ])

        mock_player1.add_cards.assert_has_calls([
            call(self.first_two_cards)
        ])

        mock_player2.add_cards.assert_has_calls([
            call(self.next_two_cards)
        ])

        # mock_player1.add_cards.assert_called_with(self.first_two_cards)
        # mock_player2.add_cards.assert_called_with(self.next_two_cards)

    def test_removes_player_if_not_willing_to_make_bet(self):
        deck = MagicMock()
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        mock_player1.wants_to_fold.return_value = True
        mock_player2.wants_to_fold.return_value = False

        players = [mock_player1, mock_player2]

        game_round = GameRound(deck = deck, players = players)
        game_round.play()

        self.assertEqual(
            game_round.players,
            [mock_player2]
        )

    def test_deals_same_community_cards_to_all_players(self):
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
    
        mock_player1.wants_to_fold.return_value = False
        mock_player2.wants_to_fold.return_value = False

        players = [mock_player1, mock_player2]
        
        mock_deck = MagicMock()
    
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card        
        ]

        game_round = GameRound(deck = mock_deck, players = players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(3), # flop cards
            call(1), # turn card
            call(1)  # river card
        ])
        
        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card),
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)