import heapq
from typing import List


# sort
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.square_dist)
        return points[:k]

    def square_dist(self, point):
        return point[0] ** 2 + point[1] ** 2


# heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-self.squared_dist(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_dist(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))
        return [points[i] for (_, i) in heap]

    def squared_dist(self, point):
        return point[0] ** 2 + point[1] ** 2
