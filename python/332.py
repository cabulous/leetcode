from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.flight_map = defaultdict(list)
        self.res = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for start, end in tickets:
            self.flight_map[start].append(end)

        for start, itinerary in self.flight_map.items():
            itinerary.sort(reverse=True)

        self.dfs('JFK')

        return self.res[::-1]

    def dfs(self, start):
        dest_list = self.flight_map[start]
        while dest_list:
            next_dest = dest_list.pop()
            self.dfs(next_dest)
        self.res.append(start)


class Solution:

    def __init__(self):
        self.flight_map = defaultdict(list)
        self.visited = {}
        self.flights = 0
        self.res = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for start, end in tickets:
            self.flight_map[start].append(end)

        for start, itinerary in self.flight_map.items():
            itinerary.sort()
            self.visited[start] = [False] * len(itinerary)

        self.flights = len(tickets)
        self.backtrack('JFK', ['JFK'])

        return self.res

    def backtrack(self, start, route):
        if len(route) == self.flights + 1:
            self.res = route
            return True

        for i, next_dest in enumerate(self.flight_map[start]):
            if not self.visited[start][i]:
                self.visited[start][i] = True
                ret = self.backtrack(next_dest, route + [next_dest])
                self.visited[start][i] = False
                if ret:
                    return True

        return False
