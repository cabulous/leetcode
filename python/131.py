# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution:

    def __init__(self):
        self.s = ''
        self.res = []

    def partition(self, s: str) -> list[list[str]]:
        self.s = s
        self.backtrack(0, [])
        return self.res

    def backtrack(self, idx, curr):
        if idx == len(self.s):
            self.res.append(curr)
            return

        for end in range(idx, len(self.s)):
            word = self.s[idx:end + 1]
            if self.is_palindrome(word):
                self.backtrack(end + 1, curr + [word])

    def is_palindrome(self, s):
        return s == s[::-1]
