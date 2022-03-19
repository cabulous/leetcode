from collections import Counter
from typing import List


# https://leetcode.com/problems/find-array-given-subset-sums/discuss/1418799/Python-Short-solution-(update)-explained/1058826
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        return self.recover(sorted(sums))

    def recover(self, sums):
        if len(sums) == 1:
            return []

        count = Counter(sums)
        split_a, split_b = [], []
        good = False
        num = sums[-1] - sums[-2]

        for a in sums:
            b = a - num
            if count[a] > 0 and count[b] > 0:
                count[a] -= 1
                count[b] -= 1
                split_a.append(a)
                split_b.append(b)
                if b == 0:
                    good = True

        if good:
            return [num] + self.recover(split_b)

        return [-num] + self.recover(split_a)
