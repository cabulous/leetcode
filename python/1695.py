from typing import List


# https://leetcode.com/problems/maximum-erasure-value/discuss/1235666/PythonJavaC%2B%2B-Sliding-Window-and-HashMap-Clean-and-Concise-O(N)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        curr = 0
        res = 0

        for right, num in enumerate(nums):
            while left <= right and num in seen:
                seen.remove(nums[left])
                curr -= nums[left]
                left += 1
            seen.add(num)
            curr += num
            res = max(res, curr)

        return res
