class Solution:

    def __init__(self):
        self.weights = []
        self.days = 0

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        self.weights = weights
        self.days = days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def feasible(self, max_weight):
        curr_load = 0
        days_needed = 1

        for weight in self.weights:
            curr_load += weight
            if curr_load > max_weight:
                days_needed += 1
                curr_load = weight

        return days_needed <= self.days
