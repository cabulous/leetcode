from collections import Counter


# https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)

        for res, freq in count.items():
            if freq == 1:
                return res

        return -1


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones
