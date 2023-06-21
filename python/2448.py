class Solution:

    def __init__(self):
        self.nums = []
        self.cost = []

    def minCost(self, nums: list[int], cost: list[int]) -> int:
        self.nums = nums
        self.cost = cost

        left = min(nums)
        right = max(nums)
        res = self.get_cost(left)

        while left < right:
            mid = left + (right - left) // 2
            cost1, cost2 = self.get_cost(mid), self.get_cost(mid + 1)
            res = min(cost1, cost2)
            if cost1 < cost2:
                right = mid
            else:
                left = mid + 1

        return res

    def get_cost(self, target):
        return sum(abs(num - target) * cost for num, cost in zip(self.nums, self.cost))
