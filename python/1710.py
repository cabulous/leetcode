from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        capacity = truckSize
        res = 0

        for box, units in boxes:
            if capacity > box:
                capacity -= box
                res += box * units
            else:
                res += capacity * units
                return res

        return res
