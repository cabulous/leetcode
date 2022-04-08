# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748704/JavaC%2B%2BPython-Short-One-Pass-O(1)-Space
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left = 0
        res = n

        for i, ch in enumerate(s):
            left = min(left + (ch == '1') * 2, i + 1)
            right = n - 1 - i
            res = min(res, left + right)

        return res
