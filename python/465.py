import math
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

    def backtrack(self, net_profit, start_idx, num_trans):
        while start_idx < len(net_profit) and net_profit[start_idx] == 0:
            start_idx += 1

        if start_idx + 1 >= len(net_profit):
            return num_trans

        for i in range(start_idx + 1, len(net_profit)):
            if net_profit[i] + net_profit[start_idx] == 0:
                net_profit[i] += net_profit[start_idx]
                min_num_trans = self.backtrack(net_profit, start_idx + 1, num_trans + 1)
                net_profit[i] -= net_profit[start_idx]
                return min_num_trans

        min_num_trans = math.inf

        for i in range(start_idx + 1, len(net_profit)):
            if net_profit[i] * net_profit[start_idx] < 0:
                net_profit[i] += net_profit[start_idx]
                min_num_trans = min(min_num_trans, self.backtrack(net_profit, start_idx + 1, num_trans + 1))
                net_profit[i] -= net_profit[start_idx]

        return min_num_trans
