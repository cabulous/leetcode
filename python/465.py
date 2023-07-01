from collections import Counter
from typing import List


# https://leetcode.com/problems/optimal-account-balancing/discuss/95363/Easy-backtracking-%2B-greedy-solution-with-explanation-(Python-Accepted)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        count = Counter()
        for source, target, amount in transactions:
            count[source] -= amount
            count[target] += amount

        balances = []
        for amount in count.values():
            if amount != 0:
                balances.append(amount)

        return self.backtrack(balances, 0, 0)

    def backtrack(self, balance, idx, count):
        while idx < len(balance) and balance[idx] == 0:
            idx += 1

        if idx == len(balance):
            return count

        for i in range(idx + 1, len(balance)):
            if balance[i] + balance[idx] == 0:
                balance[i] += balance[idx]
                res = self.backtrack(balance, idx + 1, count + 1)
                balance[i] -= balance[idx]
                return res

        res = float('inf')
        for i in range(idx + 1, len(balance)):
            if balance[i] * balance[idx] < 0:
                balance[i] += balance[idx]
                res = min(res, self.backtrack(balance, idx + 1, count + 1))
                balance[i] -= balance[idx]

        return res
