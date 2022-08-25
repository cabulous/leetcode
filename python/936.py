from typing import List


# https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
class Solution:

    def __init__(self):
        self.stamp = []
        self.target = []
        self.res = []

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        self.stamp = list(stamp)
        self.target = list(target)

        changed = True
        while changed:
            changed = False
            for i in range(len(self.target) - len(self.stamp) + 1):
                changed |= self.check(i)

        return self.res[::-1] if self.target == ['?'] * len(self.target) else []

    def check(self, curr_idx):
        changed = False

        for i in range(len(self.stamp)):
            if self.target[curr_idx + i] == '?':
                continue
            if self.target[curr_idx + i] != self.stamp[i]:
                return False
            changed = True

        if changed:
            self.target[curr_idx:curr_idx + len(self.stamp)] = ['?'] * len(self.stamp)
            self.res.append(curr_idx)

        return changed
