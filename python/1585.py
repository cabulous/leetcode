from collections import deque


# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/discuss/843917/C%2B%2BJavaPython-O(n)
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        index = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            index[int(ch)].append(i)

        for ch in t:
            digit = int(ch)
            if not index[digit]:
                return False
            for i in range(digit):
                if index[i] and index[i][0] < index[digit][0]:
                    return False
            index[digit].popleft()

        return True
