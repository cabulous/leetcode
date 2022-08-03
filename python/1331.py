from typing import List


# https://leetcode.com/problems/rank-transform-of-an-array/discuss/489753/JavaC%2B%2BPython-HashMap
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for num in sorted(arr):
            rank.setdefault(num, len(rank) + 1)

        return list(map(rank.get, arr))
