# Pop
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        max_duplicates = 2
        i = 1
        count = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > max_duplicates:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)


# Two pointers
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        max_duplicates = 2
        j = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= max_duplicates:
                nums[j] = nums[i]
                j += 1
        return j


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        max_duplicates = 2
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
               nums[i] = n
               i += 1
        return i