from typing import List


# https://leetcode.com/problems/k-empty-slots/discuss/338640/Python-sliding-window-O(n)-with-explanation
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        on_days = [0] * len(bulbs)
        for day, pos in enumerate(bulbs):
            on_days[pos - 1] = day

        left = 0
        right = left + k + 1
        res = -1

        for pos, day in enumerate(on_days):
            if right >= len(bulbs):
                return res

            max_day = max(on_days[left], on_days[right])
            if day > max_day:
                continue

            if pos == right:
                if max_day < res or res == -1:
                    res = max_day + 1

            left = pos
            right = left + k + 1

        return res
