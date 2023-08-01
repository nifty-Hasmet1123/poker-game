# # Law of demeter = says that it's not the best idea to reach or know too much 
# # about another's object state. Card_class IV topic at 27:00
# # Launching point of the program.
from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Maxi", hand = hand1)
player2 = Player(name = "Boris", hand = hand2)
players = [player1, player2]

game_round = GameRound(deck=deck, players=players)
game_round.play()

for player in players:
    print(f"\n{player.name} receives a {player.hand}.")
    idx, hand_name, hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_string = " and ".join(hand_card_strings)
    print(f"{player.name} has a {hand_name} with a {hand_card_string}.", end = "\n\n")

winning_player = max(players)
print(f"\nThe winer is {winning_player.name}!")