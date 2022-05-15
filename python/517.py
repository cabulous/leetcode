from typing import List


# https://leetcode.com/problems/super-washing-machines/discuss/99187/JavaC%2B%2BPython-O(1)-Space
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)

        if total % n != 0:
            return -1

        target = total // n
        to_right = 0
        res = 0

        for cloth_count in machines:
            to_right = cloth_count + to_right - target
            res = max(res, abs(to_right), cloth_count - target)

        return res
