from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83645/Short-and-clear-Python-BFS%2Bstack-easy-to-understand-solution-O(n)-time-O(n)-space
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        curr_level = nestedList
        stack = []

        while curr_level:
            next_level = []
            total = 0
            for item in curr_level:
                if item.isInteger():
                    total += item.getInteger()
                else:
                    next_level.extend(item.getList())
            stack.append(total)
            curr_level = next_level

        res = 0
        for i, n in enumerate(stack[::-1]):
            res += (i + 1) * n

        return res
