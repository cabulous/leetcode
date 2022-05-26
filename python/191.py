class Solution:
    def hammingWeight(self, n):
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


class Solution:
    def hammingWeight(self, n):
        total = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                total += 1
            mask <<= 1
        return total
