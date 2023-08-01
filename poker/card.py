from typing import List

class Card():
    SUITS = ("Spades", "Hearts", "Clubs", "Diamonds")
    RANKS = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10", 
        "Jack", "Queen", "King", "Ace"
    )
     
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: Rank must be one of the following {self.RANKS}")
        
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: Suit must be one of the following {self.SUITS}")
        
        self.rank = rank
        self.rank_index = self.RANKS.index(self.rank) 
        self.suit = suit

    @classmethod
    def create_52_cards(cls) -> List['Card']:
        # Card.SUITS AND Card.RANKS and using cls basically takes the position of the Card class word
        # cls(rank, suit) can also be use as Card(rank, suit) but using cls is much
        # better because sometimes you want to change the class name and this will
        # affect all the classmethods if done like that so we use cls parameter instead.
        return [cls(rank, suit) for suit in cls.SUITS for rank in cls.RANKS]
    
    def __str__(self) -> str: # with print
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self) -> str: # without print
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit
            
    def __lt__(self, other) -> bool: 
        """For sorting values lexicographically.
        
        When you implement the __lt__ method in a class, 
        you enable instances of that class to be compared 
        using the less than operator. 
        In the context of sorting, 
        the __lt__ method is used by the sort() 
        method to determine the order of elements in a list.

        The __lt__ method takes two parameters: 
        self (representing the instance on which the method is called) 
        and other (representing the other object being compared).

        In this case, the implementation compares the score attribute of the current instance (self.score) 
        with the score attribute of the other object (other.score). 
        It uses the less than operator (<) to perform the comparison.

        The __lt__ method returns True if the score of the current instance is less than the score of the other object. 
        Otherwise, it returns False. This outcome determines the ordering of the objects during sorting.

        By defining the __lt__ method in the Equality class, you provide a way for the sort() method to 
        compare instances based on their scores and sort them accordingly.

        update: added modification for sorting by suit
        """
        if self.rank == other.rank:       # "If rank is the same."
            return self.suit < other.suit # --> "Hearts" < "Spades" evaluates to True

        return self.rank_index < other.rank_index
        # current_card_rank_index = self.RANKS.index(self.rank)
        # other_card_rank_index = self.RANKS.index(other.rank)

        # return current_card_rank_index < other_card_rank_index