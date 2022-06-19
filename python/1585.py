# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/discuss/843917/C%2B%2BJavaPython-O(n)
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        index = [[] for _ in range(10)]
        position = [0] * 10

        for i, ch in enumerate(s):
            index[int(ch)].append(i)

        for ch in t:
            digit = int(ch)
            if position[digit] >= len(index[digit]):
                return False
            for i in range(digit):
                if position[i] < len(index[i]) and index[i][position[i]] < index[digit][position[digit]]:
                    return False
            position[digit] += 1

        return True
