from collections import defaultdict
from typing import List


# https://leetcode.com/problems/optimal-account-balancing/discuss/95363/Easy-backtracking-%2B-greedy-solution-with-explanation-(Python-Accepted)
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = defaultdict(int)
        for source, target, amount in transactions:
            balances[source] -= amount
            balances[target] += amount

        net_profit = []
        for amount in balances.values():
            if amount != 0:
                net_profit.append(amount)

        return self.backtrack(net_profit, 0, 0)

    def backtrack(self, net_profit, idx, count):
        while idx < len(net_profit) and net_profit[idx] == 0:
            idx += 1

        if idx + 1 >= len(net_profit):
            return count

        for i in range(idx + 1, len(net_profit)):
            if net_profit[i] + net_profit[idx] == 0:
                net_profit[i] += net_profit[idx]
                trans_count_min = self.backtrack(net_profit, idx + 1, count + 1)
                net_profit[i] -= net_profit[idx]
                return trans_count_min

        trans_count_min = float('inf')
        for i in range(idx + 1, len(net_profit)):
            if net_profit[i] * net_profit[idx] < 0:
                net_profit[i] += net_profit[idx]
                trans_count_min = min(trans_count_min, self.backtrack(net_profit, idx + 1, count + 1))
                net_profit[i] -= net_profit[idx]

        return trans_count_min
