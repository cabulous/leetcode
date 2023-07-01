from collections import Counter
from typing import List


# https://leetcode.com/problems/optimal-account-balancing/discuss/95363/Easy-backtracking-%2B-greedy-solution-with-explanation-(Python-Accepted)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        count = Counter()
        for source, target, amount in transactions:
            count[source] -= amount
            count[target] += amount

        balances = [val for val in count.values() if val != 0]

        return self.backtrack(balances, 0, 0)

    def backtrack(self, balances, idx, count):
        while idx < len(balances) and balances[idx] == 0:
            idx += 1

        if idx == len(balances):
            return count

        for i in range(idx + 1, len(balances)):
            if balances[i] + balances[idx] == 0:
                balances[i] += balances[idx]
                res = self.backtrack(balances, idx + 1, count + 1)
                balances[i] -= balances[idx]
                return res

        res = float('inf')
        for i in range(idx + 1, len(balances)):
            if balances[i] * balances[idx] < 0:
                balances[i] += balances[idx]
                res = min(res, self.backtrack(balances, idx + 1, count + 1))
                balances[i] -= balances[idx]

        return res
