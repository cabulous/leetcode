# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        for i in range(2, n + 1):
            res = res * (2 * i - 1) * i % MOD
        return res
