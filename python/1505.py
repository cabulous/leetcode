# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/discuss/720215/The-constraint-was-not-very-helpful...-C%2B%2BPython-Clean-56ms-O(n2)-solution
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k <= 0:
            return num

        n = len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(list(num)))

        for i in range(10):
            index = num.find(str(i))
            if 0 <= index <= k:
                return num[index] + self.minInteger(num[:index] + num[index + 1:], k - index)
