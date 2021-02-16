from typing import List


# https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res
