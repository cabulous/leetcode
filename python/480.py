from collections import defaultdict
import bisect
import heapq
from typing import List


# https://leetcode.com/problems/sliding-window-median/discuss/96355/Easy-Python-O(nk)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        res = []

        for to_remove, to_add in zip(nums, nums[k:] + [0]):
            median = (window[k // 2] + window[~(k // 2)]) / 2
            res.append(median)
            window.remove(to_remove)
            bisect.insort(window, to_add)

        return res


# https://leetcode.com/problems/sliding-window-median/discuss/394302/Python-clean-solution-(easy-to-understand)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or not k:
            return []

        lo, hi = [], []
        for i in range(k):
            if len(lo) == len(hi):
                heapq.heappush(hi, -heapq.heappushpop(lo, -nums[i]))
            else:
                heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))

        res = [float(hi[0])] if k % 2 == 1 else [(hi[0] - lo[0]) / 2]
        to_remove = defaultdict(int)

        for i in range(k, len(nums)):
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))

            out_num = nums[i - k]
            if out_num > -lo[0]:
                heapq.heappush(hi, -heapq.heappop(lo))

            to_remove[out_num] += 1

            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heapq.heappop(lo)

            while hi and to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heapq.heappop(hi)

            if k % 2 == 1:
                res.append(float(hi[0]))
            else:
                res.append((hi[0] - lo[0]) / 2)

        return res
