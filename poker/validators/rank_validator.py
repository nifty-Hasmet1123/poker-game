class RankValidator():       
    @property
    def _card_rank_counts(self) -> dict:
        card_rank_counts = {}

        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

    def _ranks_with_count(self, count) -> dict:
        # when this is iterated it will be like a tuple then the [1] represents as the count in the tuple 
        # key_value = ("Ace", 2)

        filt = dict(filter(
            lambda key_value: key_value[1] == count, 
            self._card_rank_counts.items()
        ))

        return filt
    
    

    
# return {
#     rank: rank_count
#     for rank, rank_count in self._card_rank_counts.items()
#     if rank_count == count
# }

    