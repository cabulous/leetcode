# two pointer
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        if not nums:
            return []

        def twoSum(i):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1

        res = []
        n = len(nums)

        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(i)

        return res


# hashset
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        def twoSum(i):
            seen = set()
            j = i + 1
            while j < n:
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(i)

        return res
