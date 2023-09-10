MOD = 10 ** 9 + 7


# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise
class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(2, n + 1):
            next_comb = (i * 2 - 1) * i
            res = res * next_comb % MOD
        return res
