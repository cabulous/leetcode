from collections import Counter
from typing import List


# https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        count = Counter(changed)
        for num in sorted(count):
            if count[num] > count[2 * num]:
                return []
            count[2 * num] -= count[num] if num != 0 else count[num] // 2

        return list(count.elements())
