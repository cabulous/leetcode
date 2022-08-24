# https://leetcode.com/problems/rotated-digits/discuss/116530/JavaPython-O(logN)-Time-O(1)-Space
class Solution:

    def __init__(self):
        self.s1 = {0, 1, 8}
        self.s2 = {0, 1, 8, 2, 5, 6, 9}

    def rotatedDigits(self, n: int) -> int:
        return sum(self.is_good(num) for num in range(1, n + 1))

    def is_good(self, num):
        s = set(int(i) for i in str(num))
        return s.issubset(self.s2) and not s.issubset(self.s1)
