from collections import defaultdict
from typing import List


# https://leetcode.com/problems/delete-duplicate-folders-in-system/discuss/1361419/Python-Serialize-subtrees-%2B-complexity-analysis-explained
class Node:

    def __init__(self):
        self.child = defaultdict(Node)
        self.deleted = False


class Solution:

    def __init__(self):
        self.pattern = defaultdict(list)
        self.res = []

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()

        for path in sorted(paths):
            node = root
            for c in path:
                node = node.child[c]

        self.collect_pattern(root)

        for nodes in self.pattern.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        self.dfs(root, [])

        return self.res

    def collect_pattern(self, node: Node):
        key = '(' + ''.join(c + self.collect_pattern(node.child[c]) for c in node.child) + ')'
        if key != '()':
            self.pattern[key].append(node)
        return key

    def dfs(self, node: Node, path):
        for c in node.child:
            if not node.child[c].deleted:
                self.dfs(node.child[c], path + [c])
        if path:
            self.res.append(path[:])
