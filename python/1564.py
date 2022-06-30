from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)

        i = 0
        res = 0

        for room in warehouse:
            while i < len(boxes) and boxes[i] > room:
                i += 1
            if i == len(boxes):
                return res
            i += 1
            res += 1

        return res
