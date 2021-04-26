import heapq
import math
from typing import List


# Min-Heap
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(ladder_allocations, climb)
            if len(ladder_allocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
                return i
        return len(heights) - 1


# Max-Heap
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brick_allocations = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(brick_allocations, -climb)
            bricks -= climb
            if bricks < 0 and ladders == 0:
                return i
            if bricks < 0:
                bricks += -heapq.heappop(brick_allocations)
                ladders -= 1
        return len(heights) - 1


# Improved Binary Search for Final Reachable Building
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        sorted_climbs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb < 0:
                continue
            sorted_climbs.append([climb, i + 1])
        sorted_climbs.sort()

        lo, hi = 0, len(heights) - 1
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            if self.is_reachable(mi, sorted_climbs, bricks, ladders):
                lo = mi
            else:
                hi = mi - 1

        return lo

    def is_reachable(self, building_index, climbs, bricks, ladders):
        for climb_entry in climbs:
            climb = climb_entry[0]
            index = climb_entry[1]
            if index > building_index:
                continue
            if climb <= bricks:
                bricks -= climb
            elif ladders >= 1:
                ladders -= 1
            else:
                return False
        return True


# Binary Search for Final Reachable Building
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        def is_reachable(building_index):
            climbs = []
            for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
                if h2 - h1 > 0:
                    climbs.append(h2 - h1)
            climbs.sort()
            bricks_remaining = bricks
            ladders_remaining = ladders
            for climb in climbs:
                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                else:
                    return False
            return True

        lo, hi = 0, len(heights) - 1
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            if is_reachable(mi):
                lo = mi
            else:
                hi = mi - 1
        return lo


# Binary Search on Threshold (Advanced)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def solve_with_given_threshold(k):
            ladders_remaining = ladders
            bricks_remaining = bricks
            ladders_used_on_threshold = 0

            for i in range(len(heights) - 1):
                climb = heights[i + 1] - heights[i]
                if climb <= 0:
                    continue
                if climb == k:
                    ladders_used_on_threshold += 1
                    ladders_remaining -= 1
                elif climb > k:
                    ladders_remaining -= 1
                else:
                    bricks_remaining -= climb

                if ladders_remaining < 0:
                    if ladders_used_on_threshold:
                        ladders_used_on_threshold -= 1
                        ladders_remaining += 1
                        bricks_remaining -= k
                    else:
                        return [i, ladders_remaining, bricks_remaining]

                if bricks_remaining < 0:
                    return [i, ladders_remaining, bricks_remaining]

            return [len(heights) - 1, ladders_remaining, bricks_remaining]

        lo, hi = math.inf, -math.inf
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            lo = min(lo, climb)
            hi = max(hi, climb)

        if lo == math.inf:
            return len(heights) - 1

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            index_reached, ladders_remaining, bricks_remaining = solve_with_given_threshold(mi)
            if index_reached == len(heights) - 1:
                return len(heights) - 1
            if ladders_remaining > 0:
                hi = mi - 1
                continue

            next_climb = heights[index_reached + 1] - heights[index_reached]
            if bricks_remaining < next_climb and bricks_remaining < mi:
                return index_reached

            lo = mi + 1
