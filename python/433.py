from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            mutation, steps = queue.popleft()
            if mutation == end:
                return steps

            for ch in 'ACGT':
                for i in range(len(mutation)):
                    next_mutation = mutation[:i] + ch + mutation[i + 1:]
                    if next_mutation not in seen and next_mutation in bank:
                        seen.add(next_mutation)
                        queue.append((next_mutation, steps + 1))

        return -1
