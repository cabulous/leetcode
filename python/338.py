class Solution:
    def countBits(self, num):
        ans = []
        for n in range(num + 1):
            total = 0
            while n != 0:
                total += 1
                n &= (n - 1)
            ans.append(total)
        return ans


# DP: least significant bits
# P(x)=P(x / 2) + (x mod 2)
class Solution:
    def countBits(self, num):
        ans = [0] * (num + 1)
        for n in range(num + 1):
            ans[n] = ans[n >> 1] + (n & 1)
        return ans


# DP: most significant bits
# P(x + b) = P(x) + 1
class Solution:
    def countBits(self, num):
        ans = [0] * (num + 1)
        i = 0
        b = 1
        while b <= num:
            while i < b and i + b <= num:
                ans[i + b] = ans[i] + 1
                i += 1
            i = 0
            b <<= 1
        return ans
