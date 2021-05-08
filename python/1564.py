from typing import List


# Add Largest Possible Boxes from Left to Right
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        i = 0
        cnt = 0
        boxes.sort(reverse=True)

        for room in warehouse:
            while i < len(boxes) and boxes[i] > room:
                i += 1
            if i == len(boxes):
                return cnt
            cnt += 1
            i += 1

        return cnt


# Add Smallest Boxes to the Rightmost Warehouse Rooms
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])

        boxes.sort()
        cnt = 0

        for room in reversed(warehouse):
            if cnt < len(boxes) and boxes[cnt] <= room:
                cnt += 1

        return cnt
