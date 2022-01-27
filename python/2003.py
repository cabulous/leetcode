from typing import List


# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/discuss/1458486/Python-Strict-O(n)-Solution
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        parent_count = len(parents)
        seen = [0] * 100010
        res = [1] * parent_count

        if 1 not in nums:
            return res

        children = [[] for _ in range(parent_count)]

        for i in range(1, parent_count):
            children[parents[i]].append(i)

        def dfs(parent):
            if seen[nums[parent]] == 0:
                for next_parent in children[parent]:
                    dfs(next_parent)
                seen[nums[parent]] = 1

        index = nums.index(1)
        miss = 1

        while index >= 0:
            dfs(index)
            while seen[miss]:
                miss += 1
            res[index] = miss
            index = parents[index]

        return res
