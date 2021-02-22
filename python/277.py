# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from functools import lru_cache


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


class Solution:
    def __init__(self):
        self.n = 0

    @lru_cache(maxsize=None)
    def cached_knows(self, a, b):
        return knows(a, b)

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue
            if self.cached_knows(i, j) or not self.cached_knows(j, i):
                return False
        return True

    def findCelebrity(self, n: int) -> int:
        self.n = n
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        if self.is_celebrity(candidate):
            return candidate
        return -1
