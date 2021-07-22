from typing import List
from collections import defaultdict, Counter, deque


# bfs
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for w in words for c in w})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ''

        res = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])

        while queue:
            c = queue.popleft()
            res.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        if len(res) < len(in_degree):
            return ''

        return ''.join(res)


# dfs
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        reverse_adj_list = {c: [] for w in words for c in w}

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ''

        seen = {}
        res = []

        def visit(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for next_node in reverse_adj_list[node]:
                if not visit(next_node):
                    return False
            seen[node] = True
            res.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ''

        return ''.join(res)
