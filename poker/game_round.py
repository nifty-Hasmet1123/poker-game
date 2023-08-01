class GameRound():
    """A class for interacting different class object in this poker package."""
    
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self) -> None:
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()
        
        self._deal_flop_cards()
        self._make_bets()

        self._deal_turn_card()
        self._make_bets()

        self._deal_river_card()
        self._make_bets()

    # for refresher we put a protective attribute because we don't want this to run or
    # be called by the developer, it will only be run inside this GameRound class.
    def _shuffle_deck(self) -> None: 
        self.deck.shuffle_cards()

    def _deal_initial_two_cards_to_each_player(self) -> None: 
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _make_bets(self) -> None:
        for player in self.players:
            if player.wants_to_fold(): # return True
                self.players.remove(player)

    def _deal_community_cards(self, number) -> None:
        """Function for assigning number in the community card."""
        community_cards = self.deck.remove_cards(number)

        for player in self.players:
            player.add_cards(community_cards)

    def _deal_flop_cards(self) -> None:
        """Give the flop cards to each player involved."""
        self._deal_community_cards(3)

    def _deal_turn_card(self) -> None:
        """Give the turn card to each player involved."""
        self._deal_community_cards(1)

    def _deal_river_card(self) -> None:
        """Give the river card to each player involved."""
        self._deal_community_cards(1)