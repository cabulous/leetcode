from typing import List
from collections import Counter


# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        freq = sorted(count.values())

        res = 0
        removed = 0
        target = len(arr) // 2
        while removed < target:
            res += 1
            removed += freq.pop()

        return res
