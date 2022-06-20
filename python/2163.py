import heapq
import math
from typing import List


# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/discuss/1747029/Python-Explanation-with-pictures-Priority-Queue.
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        cur_min = sum(nums[:n])
        pre_min = [cur_min]
        pre_max_hp = [-x for x in nums[:n]]
        heapq.heapify(pre_max_hp)
        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(pre_max_hp)
            cur_min -= cur_pop
            cur_min += min(cur_pop, nums[i])
            pre_min.append(cur_min)
            heapq.heappush(pre_max_hp, -min(cur_pop, nums[i]))

        cur_max = sum(nums[2 * n:])
        suf_max = [cur_max]
        suf_min_hp = [x for x in nums[2 * n:]]
        heapq.heapify(suf_min_hp)
        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(suf_min_hp)
            cur_max -= cur_pop
            cur_max += max(cur_pop, nums[i])
            suf_max.append(cur_max)
            heapq.heappush(suf_min_hp, max(cur_pop, nums[i]))

        res = math.inf
        for a, b in zip(pre_min, suf_max[::-1]):
            res = min(res, a - b)

        return res
