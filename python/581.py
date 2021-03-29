from typing import List


# Sort the list and check if it's still the same number in the list.
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103052/Python-Sort-Solutions
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


# O(N), O(1)
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103067/Python-O(N)-with-O(1)-space-complexity.-No-sorting
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        def find_local_min_max(l, r):
            local_min = float('inf')
            local_max = float('-inf')
            for i in range(l, r + 1):
                if i == n:
                    break
                local_min = min(local_min, nums[i])
                local_max = max(local_max, nums[i])
            return local_min, local_max

        l, r = 0, n - 1

        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
        if l > r:
            return 0

        mini, maxi = find_local_min_max(l, r + 1)

        while l > 0 and mini < nums[l - 1]:
            l -= 1
        while r < n - 1 and maxi > nums[r + 1]:
            r += 1

        return r - l + 1
