from typing import List


# https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692939/JavaC%2B%2BPython-Sort-Solution-with-Explanation-O(mlogm)
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)

        batteries.sort()

        while batteries[-1] > total // n:
            n -= 1
            total -= batteries.pop()

        return total // n
