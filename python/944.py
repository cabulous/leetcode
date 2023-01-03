from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = zip(*strs)

        res = 0
        for col in cols:
            if list(col) != sorted(col):
                res += 1

        return res
