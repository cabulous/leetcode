from typing import List
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sum = [0]
        for num in sorted(nums):
            prefix_sum.append(prefix_sum[-1] + num)

        prefix_sum = prefix_sum[1:]
        res = []

        for query in queries:
            idx = bisect.bisect_right(prefix_sum, query)
            res.append(idx)

        return res
