from typing import List


# https://leetcode.com/problems/maximum-good-people-based-on-statements/discuss/1711216/Python3-Java-C%2B%2B-Subsets-O(n2-*-2n)
class Solution:

    def __init__(self):
        self.statements = []
        self.n = 0

    def maximumGood(self, statements: List[List[int]]) -> int:
        self.statements = statements
        self.n = len(self.statements)

        res = 0

        for num in range(1 << self.n, 1 << (self.n + 1)):
            permutation = bin(num)[3:]
            if self.valid(permutation):
                res = max(res, permutation.count('1'))

        return res

    def valid(self, permutation):
        for i in range(self.n):
            if permutation[i] == '0':
                continue
            for j in range(self.n):
                if self.statements[i][j] == 2:
                    continue
                if self.statements[i][j] == 1 and permutation[j] == '0':
                    return False
                if self.statements[i][j] == 0 and permutation[j] == '1':
                    return False
        return True
