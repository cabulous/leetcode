# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution:

    def __init__(self):
        self.res = []

    def partition(self, s: str) -> [[str]]:
        if not s:
            return []

        self.helper(s, [])
        return self.res

    def helper(self, remain, curr_list):
        if not remain:
            self.res.append(curr_list[:])
            return

        for i in range(1, len(remain) + 1):
            curr_str = remain[:i]
            if self.is_palindrome(curr_str):
                curr_list.append(curr_str)
                self.helper(remain[i:], curr_list)
                curr_list.pop()

    def is_palindrome(self, string):
        return string == string[::-1]
