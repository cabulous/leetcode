import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_ladders = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue

            heapq.heappush(used_ladders, climb)
            if len(used_ladders) <= ladders:
                continue

            bricks -= heapq.heappop(used_ladders)
            if bricks < 0:
                return i

        return len(heights) - 1


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        climbs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                climbs.append((climb, i + 1))
        climbs.sort()

        left, right = 0, len(heights) - 1
        while left < right:
            mi = left + (right - left + 1) // 2
            if self.is_reachable(mi, climbs, bricks, ladders):
                left = mi
            else:
                right = mi - 1

        return left

    def is_reachable(self, building_idx, climbs, bricks, ladders):
        for climb, idx in climbs:
            if building_idx < idx:
                continue
            if climb <= bricks:
                bricks -= climb
            elif ladders > 0:
                ladders -= 1
            else:
                return False

        return True
