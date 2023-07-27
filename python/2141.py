class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()

        total = sum(batteries)
        remain = n

        while batteries[-1] > total // remain:
            remain -= 1
            total -= batteries.pop()

        return total // remain
