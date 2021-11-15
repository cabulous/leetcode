class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# https://leetcode.com/problems/diameter-of-n-ary-tree/discuss/755068/Python3-recursion-O(n)-with-explanation-beat-98
class Solution:

    def __init__(self):
        self.res = 0

    def diameter(self, root: 'Node') -> int:
        self.dfs(root)
        return self.res

    def dfs(self, node: 'Node'):
        first = second = 0
        for kid in node.children:
            depth = self.dfs(kid)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth
        self.res = max(self.res, first + second)
        return 1 + first
