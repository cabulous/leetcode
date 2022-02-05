from functools import lru_cache
from typing import List


# https://leetcode.com/problems/remove-invalid-parentheses/discuss/606847/JavaPython-DFS-with-Memoization-Fastest-Clean-and-Concise
class Solution:

    def __init__(self):
        self.s = ''
        self.s_len = 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.s = s
        self.s_len = len(s)

        valid_parentheses = self.dfs(0, 0)
        len_max = max(map(len, valid_parentheses))
        res = filter(lambda x: len(x) == len_max, valid_parentheses)

        return list(res)

    @lru_cache()
    def dfs(self, index, count):
        res = set()

        if count < 0:
            return res

        if index == self.s_len:
            if count == 0:
                res.add('')
            return res

        if self.s[index] in ('(', ')'):
            res.update(self.dfs(index + 1, count))

        if self.s[index] == '(':
            count += 1
        elif self.s[index] == ')':
            count -= 1

        for suffix in self.dfs(index + 1, count):
            res.add(self.s[index] + suffix)

        return res
