from typing import List


class UnionFind:

    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        smallest_primes = self.sieve(max(nums) + 1)
        uf = UnionFind()

        for x in nums:
            for y in self.get_prime_factors(x, smallest_primes):
                uf.union(x, y)

        for x, y in zip(nums, sorted(nums)):
            if uf.find(x) != uf.find(y):
                return False

        return True

    def sieve(self, n):
        smallest_primes = [i for i in range(n)]
        for i in range(2, n):
            if smallest_primes[i] != i:
                continue
            for j in range(i * i, n, i):
                if smallest_primes[j] > i:
                    smallest_primes[j] = i
        return smallest_primes

    def get_prime_factors(self, num, smallest_primes):
        while num > 1:
            yield smallest_primes[num]
            num //= smallest_primes[num]
