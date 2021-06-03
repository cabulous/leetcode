from typing import List


# https://leetcode.com/problems/maximum-gap/discuss/50650/Python-bucket-sort-from-official-solution
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums_len = len(nums)
        max_num, min_num = max(nums), min(nums)

        if nums_len < 2 or max_num == min_num:
            return 0

        size = (max_num - min_num) // (nums_len - 1) or 1
        buckets = [[None, None] for _ in range((max_num - min_num) // size + 1)]

        for n in nums:
            bucket = buckets[(n - min_num) // size]
            bucket[0] = n if bucket[0] is None else min(bucket[0], n)
            bucket[1] = n if bucket[1] is None else max(bucket[1], n)

        buckets = [b for b in buckets if b[0] is not None]

        return max(buckets[i][0] - buckets[i - 1][1] for i in range(1, len(buckets)))
