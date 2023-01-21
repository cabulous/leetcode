from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.solve(res, '', 0, s, 0)
        return res

    def is_valid(self, s):
        if len(s) > 3 or len(s) == 0:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True

    def solve(self, res, output, index, s, dots):
        if dots == 3:
            if self.is_valid(s[index:]):
                res.append(output + s[index:])
            return

        for i in range(index, min(index + 3, len(s))):
            if self.is_valid(s[index:i + 1]):
                next_output = output + s[index:i + 1] + '.'
                self.solve(res, next_output, i + 1, s, dots + 1)
