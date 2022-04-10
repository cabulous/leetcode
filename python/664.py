import re


# https://leetcode.com/problems/strange-printer/discuss/233067/Python.-Recursive-approach-with-memorization
# https://leetcode.com/problems/strange-printer/discuss/106794/One-suggestion-for-all-solutions
class Solution:

    def __init__(self):
        self.memo = {}

    def strangePrinter(self, s: str) -> int:
        s = re.sub(r'(.)\1*', r'\1', s)
        return self.solve(s)

    def solve(self, s):
        if not s:
            return 0

        if s in self.memo:
            return self.memo[s]

        cost = self.solve(s[:-1]) + 1
        char_to_insert = s[-1]

        for i, ch in enumerate(s[:-1]):
            if ch == char_to_insert:
                cost = min(cost, self.solve(s[:i + 1]) + self.solve(s[i + 1:-1]))

        self.memo[s] = cost

        return cost
