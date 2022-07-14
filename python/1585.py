from collections import deque


# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/discuss/843917/C%2B%2BJavaPython-O(n)
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        index = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            index[int(ch)].append(i)

        for ch in t:
            curr_num = int(ch)
            if not index[curr_num]:
                return False
            for smaller_num in range(curr_num):
                if index[smaller_num] and index[smaller_num][0] < index[curr_num][0]:
                    return False
            index[curr_num].popleft()

        return True
