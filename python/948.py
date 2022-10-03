from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        queue = deque(sorted(tokens))
        curr_point = 0
        res = 0

        while queue and (power >= queue[0] or curr_point > 0):
            if power >= queue[0]:
                power -= queue.popleft()
                curr_point += 1
            elif curr_point > 0:
                power += queue.pop()
                curr_point -= 1
            res = max(res, curr_point)

        return res
