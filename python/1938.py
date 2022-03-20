from collections import defaultdict
from typing import List


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
        self.res = []
        self.query_by_node = []
        self.graph = []

    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        parent_count = len(parents)
        query_count = len(queries)
        root = -1

        self.res = [-1] * query_count

        self.graph = [[] for _ in range(parent_count)]
        self.query_by_node = [[] for _ in range(parent_count)]

        for i, parent in enumerate(parents):
            if parent == -1:
                root = i
            else:
                self.graph[parent].append(i)

        for i, query in enumerate(queries):
            self.query_by_node[query[0]].append((query[1], i))

        self.dfs(root)

        return self.res

    def dfs(self, u):
        self.trie_node.increase(u, 1)
        for val, idx in self.query_by_node[u]:
            self.res[idx] = self.trie_node.find_max(val)
        for v in self.graph[u]:
            self.dfs(v)
        self.trie_node.increase(u, -1)
