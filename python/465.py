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

    def backtrack(self, net_profit, start_index, trans_count):
        while start_index < len(net_profit) and net_profit[start_index] == 0:
            start_index += 1

        if start_index + 1 >= len(net_profit):
            return trans_count

        for i in range(start_index + 1, len(net_profit)):
            if net_profit[i] + net_profit[start_index] == 0:
                net_profit[i] += net_profit[start_index]
                trans_count_min = self.backtrack(net_profit, start_index + 1, trans_count + 1)
                net_profit[i] -= net_profit[start_index]
                return trans_count_min

        trans_count_min = float('inf')
        for i in range(start_index + 1, len(net_profit)):
            if net_profit[i] * net_profit[start_index] < 0:
                net_profit[i] += net_profit[start_index]
                trans_count_min = min(trans_count_min, self.backtrack(net_profit, start_index + 1, trans_count + 1))
                net_profit[i] -= net_profit[start_index]

        return trans_count_min
