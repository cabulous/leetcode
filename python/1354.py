import heapq
from typing import List


# https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC%2B%2BPython-Backtrack-OJ-is-wrong
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        total = sum(target)
        max_hp = [-x for x in target]
        heapq.heapify(max_hp)

        while True:
            num = -heapq.heappop(max_hp)
            if num == 1:
                return True

            total -= num
            if total == 1:
                return True

            if total == 0 or num - total < 0 or num % total == 0:
                return False

            num %= total
            total += num
            heapq.heappush(max_hp, -num)
