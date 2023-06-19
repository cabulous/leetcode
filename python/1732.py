class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum = 0
        res = 0

        for delta in gain:
            prefix_sum += delta
            res = max(res, prefix_sum)

        return res
