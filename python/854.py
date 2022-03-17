from collections import deque


class Solution:

    def __init__(self):
        self.s2 = ''

    def kSimilarity(self, s1: str, s2: str) -> int:
        self.s2 = s2

        queue = deque([(s1, 0)])
        seen = {s1}

        while queue:
            curr, step = queue.popleft()
            if curr == s2:
                return step
            for nxt in self.get_next_string(curr):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, step + 1))

        return -1

    def get_next_string(self, curr):
        start = 0

        while curr[start] == self.s2[start]:
            start += 1

        for i in range(start + 1, len(curr)):
            if curr[i] == self.s2[start]:
                yield curr[:start] + curr[i] + curr[start + 1:i] + curr[start] + curr[i + 1:]
