from collections import Counter
from typing import List


# https://leetcode.com/problems/stickers-to-spell-word/discuss/233915/python-12-lines-solution
class Solution:

    def __init__(self):
        self.memo = {}
        self.stickers = []

    def minStickers(self, stickers: List[str], target: str) -> int:
        self.stickers = [Counter(sticker) for sticker in stickers if set(sticker) & set(target)]
        return self.dfs(target)

    def dfs(self, target):
        if not target:
            return 0

        if target in self.memo:
            return self.memo[target]

        target_counter = Counter(target)
        res = float('inf')

        for sticker_counter in self.stickers:
            if sticker_counter[target[0]] == 0:
                continue
            remain = [letter * freq for (letter, freq) in (target_counter - sticker_counter).items()]
            nxt = self.dfs(''.join(remain))
            if nxt != -1:
                res = min(res, nxt + 1)

        self.memo[target] = -1 if res == float('inf') else res

        return self.memo[target]
