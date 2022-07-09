import heapq
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        score = [0] * len(nums)
        score[0] = nums[0]

        queue = deque([0])
        for i in range(1, len(nums)):
            while queue and queue[0] < i - k:
                queue.popleft()
            score[i] = score[queue[0]] + nums[i]
            while queue and score[queue[-1]] <= score[i]:
                queue.pop()
            queue.append(i)

        return score[-1]


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = nums[0]

        priority_queue = []
        heapq.heappush(priority_queue, (-score, 0))

        for i in range(1, n):
            while priority_queue[0][1] < i - k:
                heapq.heappop(priority_queue)
            score = nums[i] - priority_queue[0][0]
            heapq.heappush(priority_queue, (-score, i))

        return score
