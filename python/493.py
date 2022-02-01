from typing import List


# https://leetcode.com/problems/reverse-pairs/discuss/162757/Python-BIT-using-ranks-Clear-O(nlog(n))
class BIT:

    def __init__(self, n):
        self.n = n + 1
        self.freq = [0] * self.n

    def update(self, index, delta):
        while index < self.n:
            self.freq[index] += delta
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.freq[index]
            index -= index & -index
        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        new_nums = nums + [x * 2 for x in nums]
        sorted_set = sorted(list(set(new_nums)))
        tree = BIT(len(sorted_set))

        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1

        res = 0
        for n in nums[::-1]:
            res += tree.query(ranks[n] - 1)
            tree.update(ranks[n * 2], 1)

        return res
