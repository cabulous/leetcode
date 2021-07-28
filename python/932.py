from typing import List


# https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= n]
