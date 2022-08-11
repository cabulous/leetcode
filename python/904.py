from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        left = 0
        res = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            if len(count) > 2:
                res = max(res, right - left)
                while len(count) > 2:
                    count[fruits[left]] -= 1
                    if count[fruits[left]] == 0:
                        count.pop(fruits[left])
                    left += 1

        res = max(res, len(fruits) - left)

        return res
