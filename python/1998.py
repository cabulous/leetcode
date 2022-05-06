from typing import List


# https://leetcode.com/problems/gcd-sort-of-an-array/discuss/1445180/C%2B%2BPython-Union-Find-and-Sieve-and-Sorting-Clean-and-Concise
class UnionFind:

    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent.setdefault(x, x) != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        prime_factors_map = self.build_prime_factors_map(max(nums) + 1)
        uf = UnionFind()

        for x in nums:
            for y in self.get_prime_factor(x, prime_factors_map):
                uf.union(x, y)

        for x, y in zip(nums, sorted(nums)):
            if uf.find(x) != uf.find(y):
                return False

        return True

    def build_prime_factors_map(self, num):
        res = [i for i in range(num)]
        for i in range(2, num):
            if res[i] != i:
                continue
            for j in range(i * i, num, i):
                res[j] = min(res[j], i)
        return res

    def get_prime_factor(self, num, prime_factors_map):
        while num > 1:
            yield prime_factors_map[num]
            num //= prime_factors_map[num]
