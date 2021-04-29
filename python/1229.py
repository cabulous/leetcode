from typing import List
import heapq


# heap
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(slots)
        while len(slots) > 1:
            start1, end1 = heapq.heappop(slots)
            start2, end2 = slots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []


# Two pointers
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        pt1 = pt2 = 0

        while pt1 < len(slots1) and pt2 < len(slots2):
            start1, end1 = slots1[pt1]
            start2, end2 = slots2[pt2]
            left = max(start1, start2)
            right = min(end1, end2)
            if right - left >= duration:
                return [left, left + duration]
            if end1 < end2:
                pt1 += 1
            else:
                pt2 += 1

        return []
