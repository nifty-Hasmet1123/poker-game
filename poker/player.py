class Player():
    """Player class. Uses instance method from other class."""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __gt__(self, other) -> bool:
        current_player_validator_index = self.best_hand()[0]
        other_player_validator_index = other.best_hand()[0]
        
        return current_player_validator_index < other_player_validator_index
        # using the less than.
    
    # this works because when you instantiate a hand object it will need the 
    # Hand() class and in the hand class there is a method called best_rank()
    # so when dealing with this. It will act like a decorator from a different 
    # class without importing it directly in this file. 
    # so the return self.hand.best_rank() will work because you are expecting
    # that the self.hand will use the Hand class.
    def best_hand(self) -> str: 
        return self.hand.best_rank()
    
    def add_cards(self, cards) -> None:
        self.hand.add_cards(cards) 
    
    def wants_to_fold(self) -> bool:
        return False