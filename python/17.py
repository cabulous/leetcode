from typing import List


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution/284974
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']

        for d in digits:
            res = [a + b for a in res for b in letters[d]]

        return res
