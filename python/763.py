from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right_most = {ch: i for i, ch in enumerate(s)}
        left, right = 0, 0
        res = []

        for i, ch in enumerate(s):
            right = max(right, right_most[ch])
            if right == i:
                res.append(right - left + 1)
                left = i + 1

        return res
