from typing import List
from collections import Counter


# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = sorted(Counter(arr).values())

        res = 0
        removed = 0
        while removed < len(arr) // 2:
            res += 1
            removed += freq.pop()

        return res
