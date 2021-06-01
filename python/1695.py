from typing import List


# https://leetcode.com/problems/maximum-erasure-value/discuss/1235666/PythonJavaC%2B%2B-Sliding-Window-and-HashMap-Clean-and-Concise-O(N)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = dict()
        res = curr_sum = 0
        left = 0
        for right, num in enumerate(nums):
            if num in seen:
                index = seen[num]
                while left <= index:
                    del seen[nums[left]]
                    curr_sum -= nums[left]
                    left += 1
            seen[num] = right
            curr_sum += num
            res = max(res, curr_sum)
        return res


# https://leetcode.com/problems/maximum-erasure-value/discuss/1235950/Python-sliding-window-solution-explained
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = right = 0
        unique_nums = set()
        curr_sum = ans = 0

        while right < len(nums):
            if nums[right] not in unique_nums:
                curr_sum += nums[right]
                unique_nums.add(nums[right])
                right += 1
                ans = max(ans, curr_sum)
            else:
                curr_sum -= nums[left]
                unique_nums.remove(nums[left])
                left += 1

        return ans
