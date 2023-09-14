from collections import defaultdict


class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.res = []

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        for start, end in tickets:
            self.graph[start].append(end)

        for end_list in self.graph.values():
            end_list.sort(reverse=True)

        self.dfs('JFK')
        return self.res[::-1]

    def dfs(self, start):
        end_list = self.graph[start]
        while end_list:
            next_start = end_list.pop()
            self.dfs(next_start)
        self.res.append(start)
