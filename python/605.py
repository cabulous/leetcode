from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        states = [0] + flowerbed + [0]
        remaining = n

        for i in range(1, len(states) - 1):
            if states[i - 1] == states[i] == states[i + 1] == 0:
                states[i] = i
                remaining -= 1
                if remaining == 0:
                    return True

        return False
