from typing import List


# https://leetcode.com/problems/find-permutation/discuss/96650/Python-simple-O(n)-solution-in-5-lines
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = []

        for i in range(len(s)):
            if s[i] == 'I':
                res.extend(range(i + 1, len(res), -1))

        res.extend(range(len(s) + 1, len(res), -1))

        return res
