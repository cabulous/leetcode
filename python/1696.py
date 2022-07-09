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
