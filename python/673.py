class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        lengths = [1] * len(nums)
        counts = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]

        max_len = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == max_len)
