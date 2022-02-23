import heapq
from typing import List


# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        queue = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        heapq.heapify(queue)

        hi = max(lst[0] for lst in nums)
        res = [float('-inf'), float('inf')]

        while queue:
            lo, list_index, num_index = heapq.heappop(queue)
            if hi - lo < res[1] - res[0]:
                res = [lo, hi]
            if num_index + 1 == len(nums[list_index]):
                return res
            next_val = nums[list_index][num_index + 1]
            hi = max(hi, next_val)
            heapq.heappush(queue, (next_val, list_index, num_index + 1))

        return res
