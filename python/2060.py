from functools import lru_cache


# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/discuss/1550012/Python3-dp
class Solution:

    def __init__(self):
        self.s1 = ''
        self.s2 = ''

    def possiblyEquals(self, s1: str, s2: str) -> bool:
        self.s1, self.s2 = s1, s2
        return self.dfs(0, 0, 0)

    def get_candidates(self, s):
        res = [int(s)]

        if len(s) == 2:
            if s[1] != '0':
                res.append(int(s[0]) + int(s[1]))
            return res

        if len(s) == 3:
            if s[1] != '0':
                res.append(int(s[:1]) + int(s[1:]))
            if s[2] != '0':
                res.append(int(s[:2]) + int(s[2:]))
            if s[1] != '0' and s[2] != '0':
                res.append(int(s[0]) + int(s[1]) + int(s[2]))

        return res

    @lru_cache(None)
    def dfs(self, i, j, diff):
        if i == len(self.s1) and j == len(self.s2):
            return diff == 0

        if i < len(self.s1) and self.s1[i].isdigit():
            next_i = i
            while next_i < len(self.s1) and self.s1[next_i].isdigit():
                next_i += 1
            for x in self.get_candidates(self.s1[i:next_i]):
                if self.dfs(next_i, j, diff - x):
                    return True

        elif j < len(self.s2) and self.s2[j].isdigit():
            next_j = j
            while next_j < len(self.s2) and self.s2[next_j].isdigit():
                next_j += 1
            for x in self.get_candidates(self.s2[j:next_j]):
                if self.dfs(i, next_j, diff + x):
                    return True

        elif diff == 0:
            if i < len(self.s1) and j < len(self.s2) and self.s1[i] == self.s2[j]:
                return self.dfs(i + 1, j + 1, 0)

        elif diff > 0:
            if i < len(self.s1):
                return self.dfs(i + 1, j, diff - 1)

        else:
            if j < len(self.s2):
                return self.dfs(i, j + 1, diff + 1)

        return False
