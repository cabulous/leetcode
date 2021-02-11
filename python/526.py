# https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms
class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, nums):
            if i == 1:
                return 1
            return sum(
                count(i - 1, nums - {d})
                for d in nums
                if d % i == 0 or i % d == 0
            )

        return count(n, set(range(1, n + 1)))
