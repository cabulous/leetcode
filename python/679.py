import itertools
import math
from typing import List


# https://leetcode.com/problems/24-game/discuss/107675/Short-Python
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)
        return any(
            self.judgePoint24([x] + rest)
            for a, b, *rest in itertools.permutations(cards)
            for x in {a + b, a - b, a * b, b and a / b}
        )


# https://leetcode.com/problems/24-game/discuss/164936/Short-intuitive-python-solution
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)

        if len(cards) == 1:
            return math.isclose(cards[0], 24)

        for i in range(n):
            for j in range(n):
                if i != j:
                    rest = [cards[k] for k in range(n) if k != i and k != j]
                    if self.judgePoint24(rest + [cards[i] + cards[j]]):
                        return True
                    if self.judgePoint24(rest + [cards[i] * cards[j]]):
                        return True
                    if self.judgePoint24(rest + [cards[i] - cards[j]]):
                        return True
                    if self.judgePoint24(rest + [cards[j] - cards[i]]):
                        return True
                    if cards[i] != 0 and self.judgePoint24(rest + [cards[j] / cards[i]]):
                        return True
                    if cards[j] != 0 and self.judgePoint24(rest + [cards[i] / cards[j]]):
                        return True

        return False
