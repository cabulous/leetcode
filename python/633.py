# https://leetcode.com/problems/sum-of-square-numbers/discuss/104973/Python-Straightforward-with-Explanation
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_square(n):
            return int(n ** 0.5) ** 2 == n

        return any(is_square(c - a * a) for a in range(int(c ** 0.5) + 1))


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
