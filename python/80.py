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
