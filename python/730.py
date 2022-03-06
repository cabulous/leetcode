from collections import deque, defaultdict
from functools import lru_cache

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109508/N2-DP-Python-with-Explanation/979094
class Solution:

    def __init__(self):
        self.forward = deque()
        self.backward = []

    def countPalindromicSubsequences(self, s: str) -> int:
        forward_dic = defaultdict(lambda: -1)
        for i in reversed(range(len(s))):
            ch = s[i]
            forward_dic[ch] = i
            self.forward.appendleft(forward_dic.copy())

        backward_dic = defaultdict(lambda: -1)
        for i, ch in enumerate(s):
            backward_dic[ch] = i
            self.backward.append(backward_dic.copy())

        return self.dp(0, len(s) - 1) - 1

    @lru_cache(None)
    def dp(self, i, j):
        if i > j:
            return 1

        res = 1

        for letter in ('a', 'b', 'c', 'd'):
            forward_index = self.forward[i][letter]
            backward_index = self.backward[j][letter]

            if forward_index == -1 or backward_index < i or forward_index > j:
                continue

            res += 1

            if forward_index < backward_index:
                res += self.dp(forward_index + 1, backward_index - 1)

        return res % MOD
