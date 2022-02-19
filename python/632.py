import heapq
from typing import List


# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        queue = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        heapq.heapify(queue)

        right = max(lst[0] for lst in nums)
        res = [float('-inf'), float('inf')]

        while queue:
            left, list_index, num_index = heapq.heappop(queue)
            if right - left < res[1] - res[0]:
                res = [left, right]
            if num_index + 1 == len(nums[list_index]):
                return res
            val = nums[list_index][num_index + 1]
            right = max(right, val)
            heapq.heappush(queue, (val, list_index, num_index + 1))

        return res
