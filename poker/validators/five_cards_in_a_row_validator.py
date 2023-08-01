from typing import List

class FiveCardValidator():
    @property
    def _collection_of_five_straight_cards_in_a_row(self) -> List[list]:
        index = 0 
        final_index = len(self.cards) - 1 
        collection_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index: 
            next_five_cards = self.cards[index: index + 5]
            next_five_rank_indices = [
                card.rank_index
                for card in next_five_cards
            ]
            
            if self._every_element_increasing_by_1(rank_indexes = next_five_rank_indices):
                collection_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1

        return collection_of_five_straight_cards_in_a_row

    def _every_element_increasing_by_1(self, rank_indexes) -> bool:
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]

        straight_consecutive_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )  

        return rank_indexes == straight_consecutive_indexes