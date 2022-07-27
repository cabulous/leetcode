from typing import List


# https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {str(cells): n}
        curr = cells[:]
        remaining = n

        while remaining:
            seen.setdefault(str(curr), remaining)
            prev = curr[:]

            remaining -= 1

            curr[0] = curr[-1] = 0
            for i in range(1, 7):
                if prev[i - 1] == prev[i + 1]:
                    curr[i] = 1
                else:
                    curr[i] = 0

            if str(curr) in seen:
                remaining %= seen[str(curr)] - remaining

        return curr
