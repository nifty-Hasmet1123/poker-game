# importing another class is subjectable to debate
# some say it is good to unittest a single class only
# while others say that it is common to unittest object
# especially in object-oriented-programming.
from poker.card import Card
from poker.deck import Deck
from unittest.mock import patch
import unittest

class DeckTest(unittest.TestCase):
    def test_deck_has_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck._cards, # protected attribute
            []   
        )
    
    def test_adds_cards_to_its_collection(self):
        card = Card(rank = "5", suit = "Clubs") 
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck._cards,
            [card]
        )

    @patch("random.shuffle")
    def test_shuffles_card_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank = "7", suit = "Spades"),
            Card(rank = "9", suit = "Hearts")
        ]

        deck.add_cards(cards)
        deck.shuffle_cards()

        # this is how to passed in an argument using the patch
        # using the assert_called_once_with(<arguments>)
        mock_shuffle.assert_called_once_with(cards)
                

    # def test_cards_has_shuffle(self): # this also works in shuffling decks
    #     deck = Deck()

    #     new_52_cards = Card.create_52_cards()
    #     deck.add_cards(new_52_cards)

    #     shuffled_cards = deck.shuffle_cards()

    #     self.assertEqual(
    #         shuffled_cards,
    #         deck._cards
    #     )

    def test_remove_specified_number_of_cards_on_deck(self):
        ace = Card(rank = "Ace", suit = "Hearts")
        eight = Card(rank = "8", suit = "Spades")
        cards = [ace, eight]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck._cards,
            [eight]
        )

    def test_deck_has_length_function(self):
        deck = Deck()
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Jack", suit = "Hearts")
        ]

        deck.add_cards(cards)
        
        self.assertEqual(len(deck), 2)