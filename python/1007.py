from typing import List


# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC%2B%2BPython-Different-Ideas
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for num in [tops[0], bottoms[0]]:
            if all(num in pair for pair in zip(tops, bottoms)):
                return len(tops) - max(tops.count(num), bottoms.count(num))
        return -1
