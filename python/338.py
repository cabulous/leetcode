class Solution:
    def countBits(self, num):
        res = []
        for n in range(num + 1):
            count = 0
            while n != 0:
                count += 1
                n &= (n - 1)
            res.append(count)
        return res


# DP: least significant bits
# P(x)=P(x / 2) + (x mod 2)
class Solution:
    def countBits(self, num):
        res = [0] * (num + 1)
        for i in range(len(res)):
            res[i] = res[i // 2] + (i % 2)
        return res
