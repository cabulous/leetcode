from typing import List


class Solution:

    def __init__(self):
        self.s = ''
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.backtrack(0, '', 0)
        return self.res

    def backtrack(self, index, curr, dots):
        if dots == 3:
            if self.is_valid(self.s[index:]):
                self.res.append(curr + self.s[index:])
            return

        for end in range(index, min(index + 3, len(self.s))):
            piece = self.s[index:end + 1]
            if self.is_valid(piece):
                self.backtrack(end + 1, curr + piece + '.', dots + 1)

    def is_valid(self, s):
        if len(s) == 0 or 3 < len(s):
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True
