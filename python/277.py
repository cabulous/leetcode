def knows(a: int, b: int) -> bool:
    pass


# https://leetcode.com/problems/find-the-celebrity/discuss/71228/JavaPython-O(n)-calls-O(1)-space-easy-to-understand-solution
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        for i in range(n):
            if knows(candidate, i):
                candidate = i

        if any(knows(candidate, i) for i in range(candidate)):
            return -1

        if any(not knows(i, candidate) for i in range(n)):
            return -1

        return candidate
