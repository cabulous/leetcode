# https://leetcode.com/problems/minimum-window-subsequence/discuss/512645/Easy-To-Understand-%3A-Sliding-window-2-pointer-Find-then-Improve
class Solution:

    def __init__(self):
        self.s1 = ''
        self.s2 = ''

    def minWindow(self, s1: str, s2: str) -> str:
        self.s1, self.s2 = s1, s2
        s1_pointer = 0
        min_len = float('inf')
        res = ''

        while s1_pointer < len(s1):
            end = self.get_end_pointer(s1_pointer)

            if end is None:
                break

            start = self.get_best_start_pointer(end)

            curr_len = end - start + 1
            if curr_len < min_len:
                min_len = curr_len
                res = s1[start:end + 1]

            s1_pointer = start + 1

        return res

    def get_end_pointer(self, s1_pointer):
        s2_pointer = 0
        while s1_pointer < len(self.s1):
            if self.s1[s1_pointer] == self.s2[s2_pointer]:
                s2_pointer += 1
                if s2_pointer == len(self.s2):
                    break
            s1_pointer += 1
        return s1_pointer if s2_pointer == len(self.s2) else None

    def get_best_start_pointer(self, s1_pointer):
        s2_pointer = len(self.s2) - 1
        while s2_pointer >= 0:
            if self.s1[s1_pointer] == self.s2[s2_pointer]:
                s2_pointer -= 1
            s1_pointer -= 1
        return s1_pointer + 1
