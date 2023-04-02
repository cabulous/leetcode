import bisect


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res = [0] * len(spells)

        for i, spell in enumerate(spells):
            left = 0
            right = len(potions)
            while left < right:
                mid = left + (right - left) // 2
                if potions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid
            res[i] = len(potions) - left

        return res
