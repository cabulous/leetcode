import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=self.square_dist)[:k]

    def square_dist(self, point):
        return point[0] ** 2 + point[1] ** 2


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-self.square_dist(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.square_dist(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]

    def square_dist(self, point):
        return point[0] ** 2 + point[1] ** 2
