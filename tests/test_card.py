from poker.card import Card
import unittest

class CardTest(unittest.TestCase):
    def test_card_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_card_has_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")
    
    def test_know_its_rank_index(self):
        card = Card(rank = "Ace", suit = "Spades")
        self.assertEqual(card.rank_index, 12)

    def test_string_representation(self):
        card = Card(rank = "7", suit = "Diamonds")
        self.assertEqual(card.__str__(), f"{card.rank} of {card.suit}")
        # or 
        # self.assertEqual(str(card), f"{card.rank} of {card.suit}")

    def test_has_repr(self):
        card = Card(rank = "5", suit = "Spades")
        self.assertEqual(card.__repr__(), "Card('5', 'Spades')")

    def test_card_has_four_suit(self):
        self.assertEqual(
            Card.SUITS, 
            ("Spades", "Hearts", "Clubs", "Diamonds")
        )

    def test_card_has_thirteen_ranks(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9",
                "10", "Jack", "Queen", "King", "Ace"
            )
        )

    def test_card_not_in_ranks(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Clubs")
    
    def test_card_not_in_suits(self):
        self.assertRaises(ValueError, lambda: Card(rank = "2", suit = "Spam")) 
        # second argument of assertRaises accepts a callable object hence 
        # lambda was use and to delay the execution of Card class for it to properly
        # read the raise error inside the Card class. 
        #  if we pass Card(rank="2", suit="Spam") 
        # directly as the second argument, 
        # the constructor will be called before the assertRaises method is executed.

    def test_create_52_cards(self):
        card = Card.create_52_cards()
        self.assertEqual(len(card), 52)

        self.assertEqual(
            card[0],
            Card(rank = "2", suit = "Spades")
        )

        self.assertEqual(
            card[-1],
            Card(rank = "Ace", suit = "Diamonds")
        )
    
    def test_considered_two_cards_are_equal(self):
        self.assertEqual(
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs")
        )

    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_spades = Card(rank = "King", suit = "Spades")
        evaluation = queen_of_spades < king_of_spades

        self.assertEqual(
            evaluation,
            True,
            "The sorting algorithm is not sorting the lower card first"
        )

    def test_sort_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades")
        five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        five_of_hearts = Card(rank = "5", suit = "Hearts")
        eight_of_hearts = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        unsorted_cards = [
            five_of_diamonds, two_of_spades, five_of_hearts, 
            ace_of_clubs, eight_of_hearts
        ]

        unsorted_cards.sort() # this is being done using the __lt__ method in the card.py file
        
        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades, five_of_diamonds, five_of_hearts,
                eight_of_hearts, ace_of_clubs
            ]
        )