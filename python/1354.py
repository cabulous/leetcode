import heapq
from typing import List


# https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC%2B%2BPython-Backtrack-OJ-is-wrong
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            x = -heapq.heappop(target)
            total -= x
            if x == 1 or total == 1:
                return True
            if x < total or total == 0 or x % total == 0:
                return False
            x %= total
            total += x
            heapq.heappush(target, -x)


# Working Backward with Optimizations
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        total = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)

        while -target[0] > 1:
            largest = -target[0]
            rest = total - largest
            if rest == 1:
                return True
            x = largest % rest
            if x == 0 or x == largest:
                return False
            heapq.heapreplace(target, -x)
            total = total - largest + x

        return True


# Working Backward
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        total = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)

        while -target[0] > 1:
            largest = -target[0]
            x = largest - (total - largest)
            if x < 1:
                return False
            heapq.heapreplace(target, -x)
            total = total - largest + x

        return True
