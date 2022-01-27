from typing import List


# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/discuss/1458486/Python-Strict-O(n)-Solution
class Solution:

    def __init__(self):
        self.nums = []
        self.seen = [0] * 100010
        self.children = []

    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        self.nums = nums
        parent_count = len(parents)
        res = [1] * parent_count

        if 1 not in nums:
            return res

        self.children = [[] for _ in range(parent_count)]
        for i in range(1, parent_count):
            self.children[parents[i]].append(i)

        index = nums.index(1)
        miss = 1

        while index >= 0:
            self.dfs(index)
            while self.seen[miss] == 1:
                miss += 1
            res[index] = miss
            index = parents[index]

        return res

    def dfs(self, parent):
        if self.seen[self.nums[parent]] == 0:
            for next_parent in self.children[parent]:
                self.dfs(next_parent)
            self.seen[self.nums[parent]] = 1
