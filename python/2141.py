class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        total = sum(batteries)
        remain = n
        batteries.sort()

        while batteries[-1] > total // remain:
            remain -= 1
            total -= batteries.pop()

        return total // remain
