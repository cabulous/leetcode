from typing import List


# https://leetcode.com/problems/maximum-erasure-value/discuss/1235666/PythonJavaC%2B%2B-Sliding-Window-and-HashMap-Clean-and-Concise-O(N)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        curr = 0
        left = 0
        res = 0

        for right, num in enumerate(nums):
            if num in seen:
                index = seen[num]
                while left <= index:
                    del seen[nums[left]]
                    curr -= nums[left]
                    left += 1
            seen[num] = right
            curr += num
            res = max(res, curr)

        return res
