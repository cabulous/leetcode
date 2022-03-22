# https://leetcode.com/problems/champagne-tower/discuss/118711/JavaC%2B%2BPython-1D-DP-O(R)-space
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [poured] + [0] * query_row

        for row in range(1, query_row + 1):
            for i in reversed(range(row + 1)):
                res[i] = max(res[i] - 1, 0) / 2 + max(res[i - 1] - 1, 0) / 2

        return min(res[query_glass], 1)
