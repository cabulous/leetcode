from typing import List


# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0: 0}
        count = 0
        res = 0

        for i, num in enumerate(nums, 1):
            count += 1 if num == 1 else -1

            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i

        return res
