# https://leetcode.com/problems/sum-of-square-numbers/discuss/104973/Python-Straightforward-with-Explanation
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(self.is_square(c - a * a) for a in range(int(c ** 0.5) + 1))

    def is_square(self, n: int) -> bool:
        return int(n ** 0.5) ** 2 == n


# https://leetcode.com/problems/sum-of-square-numbers/discuss/353607/Python-Easy-Solution%3A-Two-Pointers
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr_c = int(c ** 0.5)
        left, right = 0, sqr_c

        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            if res < c:
                left += 1
            else:
                right -= 1

        return False
