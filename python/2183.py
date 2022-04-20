import math
from collections import Counter
from typing import List


# https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785027/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = Counter(math.gcd(num, k) for num in nums)
        res = 0

        for a in count:
            for b in count:
                if a <= b and a * b % k == 0:
                    res += count[a] * count[b] if a < b else count[a] * (count[a] - 1) // 2

        return res
