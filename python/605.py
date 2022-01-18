from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        remaining = n
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1]:
                flowerbed[i] = 1
                remaining -= 1
                if remaining == 0:
                    return True

        return False
