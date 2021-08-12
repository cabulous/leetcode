from typing import List
from collections import Counter


# https://leetcode.com/problems/array-of-doubled-pairs/discuss/203183/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for num in sorted(count, key=lambda x: abs(x)):
            if count[num] > count[num * 2]:
                return False
            count[num * 2] -= count[num]
        return True


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)

        for num in sorted(arr, key=lambda x: abs(x)):
            if count[num] == 0:
                continue
            if count[num * 2] == 0:
                return False
            count[num] -= 1
            count[num * 2] -= 1

        return True
