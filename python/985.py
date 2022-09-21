from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_total = sum(num for num in nums if num % 2 == 0)
        res = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_total -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_total += nums[idx]
            res.append(even_total)

        return res
