from typing import List


# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution:

    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        self.helper(s, [])
        return self.res

    def helper(self, remain, curr_list):
        if not remain:
            self.res.append(curr_list[:])
            return

        for end_index in range(1, len(remain) + 1):
            word = remain[:end_index]
            if self.is_palindrome(word):
                curr_list.append(word)
                self.helper(remain[end_index:], curr_list)
                curr_list.pop()

    def is_palindrome(self, string):
        return string == string[::-1]
