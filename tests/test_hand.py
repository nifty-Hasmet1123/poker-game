from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator
import unittest

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_receives_and_store_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        jack_of_hearts = Card(rank = "Jack", suit = "Hearts")

        cards = [    # fixes issues in the init method sort func of Hand class.
            ace_of_spades, 
            jack_of_hearts
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                jack_of_hearts,
                ace_of_spades
            ],
            "The list is returning in different sequence, Sort it properly."
        )
    
    def test_shows_all_its_in_technical_representations(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "7", suit = "Diamonds")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(hand.__repr__(), "7 of Diamonds, Ace of Spades")

    def test_interacts_with_validator_to_get_winning_hand(self):
        """A advance technique of unittesting to simplify the test"""
        class HandWithOneValidator(Hand): 
            VALIDATORS = (PairValidator,) # need to have comma for a tuple.

        one_pair = [
            Card(rank = rank, suit = "Diamonds")
            for rank in ["Ace", "Ace"]
        ]

        hand = HandWithOneValidator()
        hand.add_cards(cards = one_pair)

        self.assertEqual(
            hand.best_rank(),
            (0, "Pair", one_pair)
        )        