class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        curr_max = max(candies)
        return [candy + extraCandies >= curr_max for candy in candies]
