import heapq


# https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.small_max_heap) == len(self.large_min_heap):
            heapq.heappush(self.large_min_heap, -heapq.heappushpop(self.small_max_heap, -num))
        else:
            heapq.heappush(self.small_max_heap, -heapq.heappushpop(self.large_min_heap, num))

    def findMedian(self) -> float:
        if len(self.small_max_heap) == len(self.large_min_heap):
            return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2.0
        return float(self.large_min_heap[0])
