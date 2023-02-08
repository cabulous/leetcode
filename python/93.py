class Solution:

    def __init__(self):
        self.s = ''
        self.res = []

    def restoreIpAddresses(self, s: str) -> list[str]:
        self.s = s
        self.backtrack(0, [], 0)
        return self.res

    def backtrack(self, idx, curr, dots):
        if dots == 3:
            piece = self.s[idx:]
            if self.is_valid(piece):
                self.res.append(''.join(curr + [piece]))
            return

        for end in range(idx, min(idx + 3, len(self.s))):
            piece = self.s[idx:end + 1]
            if self.is_valid(piece):
                self.backtrack(end + 1, curr + [piece + '.'], dots + 1)

    def is_valid(self, piece):
        if len(piece) == 0 or len(piece) > 3:
            return False
        if len(piece) > 1 and piece[0] == '0':
            return False
        if int(piece) > 255:
            return False
        return True
