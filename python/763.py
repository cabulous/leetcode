from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        left = right = 0
        res = []

        for i, ch in enumerate(s):
            right = max(right, last[ch])
            if right == i:
                res.append(right - left + 1)
                left = i + 1

        return res
