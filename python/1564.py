from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)

        box_idx = 0
        res = 0

        for room in warehouse:
            while box_idx < len(boxes) and boxes[box_idx] > room:
                box_idx += 1
            if box_idx == len(boxes):
                return res
            box_idx += 1
            res += 1

        return res
