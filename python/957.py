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
            curr = [0] + [prev[i - 1] ^ prev[i + 1] ^ 1 for i in range(1, 7)] + [0]

            if str(curr) in seen:
                n %= seen[str(curr)] - n

        return curr
