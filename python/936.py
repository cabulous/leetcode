from typing import List


# https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
class Solution:

    def __init__(self):
        self.stamp = []
        self.stamp_len = 0
        self.target = []
        self.target_len = 0
        self.res = []

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        self.stamp = list(stamp)
        self.stamp_len = len(stamp)
        self.target = list(target)
        self.target_len = len(target)

        changed = True
        while changed:
            changed = False
            for i in range(self.target_len - self.stamp_len + 1):
                changed |= self.check(i)

        return self.res[::-1] if self.target == ['?'] * self.target_len else []

    def check(self, curr_idx):
        changed = False

        for i in range(self.stamp_len):
            if self.target[curr_idx + i] == '?':
                continue
            if self.target[curr_idx + i] != self.stamp[i]:
                return False
            changed = True

        if changed:
            self.target[curr_idx:curr_idx + self.stamp_len] = ['?'] * self.stamp_len
            self.res.append(curr_idx)

        return changed
