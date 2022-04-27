from itertools import product
from typing import List


# https://leetcode.com/problems/brace-expansion-ii/discuss/317623/Python3-Clear-and-Short-Recursive-Solution
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        start = 0

        for i, ch in enumerate(expression):
            if ch == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif ch == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif ch == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([ch])

        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, product(*group)))

        return sorted(word_set)
