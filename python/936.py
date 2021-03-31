from typing import List


# Work Backwards
# https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        s, t = list(stamp), list(target)
        res = []

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                res.append(i)
            return changed

        changed = True

        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)

        return res[::-1] if t == ['?'] * n else []
