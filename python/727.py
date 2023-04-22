# https://leetcode.com/problems/minimum-window-subsequence/discuss/512645/Easy-To-Understand-%3A-Sliding-window-2-pointer-Find-then-Improve
class Solution:

    def __init__(self):
        self.s1 = ''
        self.s2 = ''

    def minWindow(self, s1: str, s2: str) -> str:
        self.s1 = s1
        self.s2 = s2

        s1_reader = 0
        min_len = float('inf')
        res = ''

        while s1_reader < len(s1):
            end = self.get_end(s1_reader)
            if end is None:
                return res

            start = self.get_start(end)
            curr_len = end - start + 1
            if curr_len < min_len:
                min_len = curr_len
                res = s1[start:end + 1]

            s1_reader = start + 1

        return res

    def get_end(self, s1_reader):
        s2_reader = 0
        while s1_reader < len(self.s1):
            if self.s1[s1_reader] == self.s2[s2_reader]:
                s2_reader += 1
                if s2_reader == len(self.s2):
                    return s1_reader
            s1_reader += 1
        return None

    def get_start(self, s1_reader):
        s2_reader = len(self.s2) - 1
        while s2_reader >= 0:
            if self.s1[s1_reader] == self.s2[s2_reader]:
                s2_reader -= 1
            s1_reader -= 1
        return s1_reader + 1
