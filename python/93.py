from typing import List


class Solution:

    def __init__(self):
        self.s = ''
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.solve('', 0, 0)
        return self.res

    def is_valid(self, s):
        if len(s) > 3 or len(s) == 0:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True

    def solve(self, curr, index, dots):
        if dots == 3:
            if self.is_valid(self.s[index:]):
                self.res.append(curr + self.s[index:])
            return

        for i in range(index, min(index + 3, len(self.s))):
            if self.is_valid(self.s[index:i + 1]):
                next_output = curr + self.s[index:i + 1] + '.'
                self.solve(next_output, i + 1, dots + 1)
