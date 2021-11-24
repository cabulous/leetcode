from collections import defaultdict
from typing import List


class DisjointSetUnion(object):

    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
        if self.rank[px] > self.rank[py]:
            px, py = py, px
        self.parent[px] = py
        self.rank[py] += self.rank[px]
        return py


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        dsu = DisjointSetUnion(max(nums))
        num_factor_map = {}

        for num in nums:
            prime_factors = list(set(self.factor_decompose(num)))
            num_factor_map[num] = prime_factors[0]
            for i in range(1, len(prime_factors)):
                dsu.union(prime_factors[i - 1], prime_factors[i])

        max_size = 0
        group_count = defaultdict(int)
        for num in nums:
            group_id = dsu.find(num_factor_map[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size

    def factor_decompose(self, num):
        factor = 2
        prime_factors = []
        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num //= factor
            else:
                factor += 1
        prime_factors.append(num)
        return prime_factors
