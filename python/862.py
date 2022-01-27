from collections import deque
from typing import List


# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[0, 0]])
        prefix_sum = 0
        res = float('inf')

        for i, num in enumerate(nums):
            prefix_sum += num
            while queue and prefix_sum - queue[0][1] >= k:
                res = min(res, i - queue.popleft()[0] + 1)
            while queue and prefix_sum <= queue[-1][1]:
                queue.pop()
            queue.append([i + 1, prefix_sum])

        return res if res != float('inf') else -1
