from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        queue = deque(sorted(tokens))
        curr = 0
        res = 0

        while queue and (queue[0] <= power or curr != 0):
            if queue[0] <= power:
                power -= queue.popleft()
                curr += 1
            else:
                power += queue.pop()
                curr -= 1
            res = max(res, curr)

        return res
