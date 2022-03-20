from collections import defaultdict
from typing import List


# https://leetcode.com/problems/maximum-genetic-difference-query/discuss/1344913/C%2B%2BJavaPython-DFS-and-Trie-and-Compute-queries-by-nodes-Clean-and-Concise
class TrieNode:

    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.go = 0

    def increase(self, number, delta):
        curr = self
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            curr = curr.child[bit]
            curr.go += delta

    def find_max(self, number):
        curr = self
        res = 0
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if (1 - bit) in curr.child and curr.child[1 - bit].go > 0:
                curr = curr.child[1 - bit]
                res |= (1 << i)
            else:
                curr = curr.child[bit]
        return res


class Solution:

    def __init__(self):
        self.trie_node = TrieNode()
        self.query_by_node = []
        self.graph = []
        self.res = []

    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(len(parents))]
        root = -1

        for i, parent in enumerate(parents):
            if parent == -1:
                root = i
            else:
                self.graph[parent].append(i)

        self.query_by_node = [[] for _ in range(len(parents))]

        for i, query in enumerate(queries):
            self.query_by_node[query[0]].append((query[1], i))

        self.res = [-1] * len(queries)
        self.dfs(root)

        return self.res

    def dfs(self, node):
        self.trie_node.increase(node, 1)
        for val, index in self.query_by_node[node]:
            self.res[index] = self.trie_node.find_max(val)
        for next_node in self.graph[node]:
            self.dfs(next_node)
        self.trie_node.increase(node, -1)
