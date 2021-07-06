from typing import List
from collections import Counter


# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        frequencies = list(counts.values())
        frequencies.sort()

        res = 0
        removed = 0
        half = len(arr) // 2

        while removed < half:
            res += 1
            removed += frequencies.pop()

        return res


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        frequencies = list(counts.values())
        max_freq = max(frequencies)
        buckets = [0] * (max_freq + 1)

        for freq in frequencies:
            buckets[freq] += 1

        res = 0
        removed = 0
        half = len(arr) // 2
        freq = max_freq

        while removed < half:
            res += 1
            while buckets[freq] == 0:
                freq -= 1
            removed += freq
            buckets[freq] -= 1

        return res
