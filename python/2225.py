from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses_count = Counter()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses_count[loser] += 1

        zero_loss = []
        one_loss = []
        for player in sorted(players):
            if losses_count[player] == 0:
                zero_loss.append(player)
            elif losses_count[player] == 1:
                one_loss.append(player)

        return [zero_loss, one_loss]
