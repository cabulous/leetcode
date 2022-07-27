from typing import List


# https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {str(cells): n}
        curr = cells[:]

        while n:
            seen.setdefault(str(curr), n)
            prev = curr[:]

            n -= 1

            curr[0] = curr[-1] = 0
            for i in range(1, 7):
                if prev[i - 1] == prev[i + 1]:
                    curr[i] = 1
                else:
                    curr[i] = 0

            if str(curr) in seen:
                n %= seen[str(curr)] - n

        return curr
