from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)

        for num in sorted(arr, key=lambda x: abs(x)):
            if count[num] == 0:
                continue
            if count[2 * num] == 0:
                return False
            count[2 * num] -= 1
            count[num] -= 1

        return True


# https://leetcode.com/problems/array-of-doubled-pairs/discuss/203183/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for num in sorted(count, key=lambda x: abs(x)):
            if count[num] > count[2 * num]:
                return False
            count[2 * num] -= count[num]
        return True
