from typing import List


# https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {str(cells): n}

        while n:
            seen.setdefault(str(cells), n)
            n -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                n %= seen[str(cells)] - n

        return cells
