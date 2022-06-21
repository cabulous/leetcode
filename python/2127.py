from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Python-Explanation-with-pictures.
class Solution:

    def __init__(self):
        self.favorite = []

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.favorite = favorite

        max_count_in_loop = self.count_in_loop()
        max_count_in_pair = self.count_in_pair()

        return max(max_count_in_loop, max_count_in_pair)

    def count_in_pair(self):
        n = len(self.favorite)
        pair = []
        visited = [False] * n

        for i in range(n):
            if self.favorite[self.favorite[i]] == i and not visited[i]:
                pair.append([i, self.favorite[i]])
                visited[i] = True
                visited[self.favorite[i]] = True

        graph = defaultdict(list)
        for i in range(n):
            graph[self.favorite[i]].append(i)

        res = 0
        for a, b in pair:
            max_arm_a = self.arm_length(graph, a, b)
            max_arm_b = self.arm_length(graph, b, a)
            res += 2 + max_arm_a + max_arm_b

        return res

    def arm_length(self, graph, start, exclude):
        res = 0
        queue = deque()

        for cand in graph[start]:
            if cand != exclude:
                queue.append([cand, 1])

        while queue:
            people, count = queue.popleft()
            res = max(res, count)
            for next_people in graph[people]:
                queue.append([next_people, count + 1])

        return res

    def count_in_loop(self):
        n = len(self.favorite)
        max_count = 0
        seen = [False] * n

        for i in range(n):
            if seen[i]:
                continue

            start = i
            people = i
            seen_people = set()

            while not seen[people]:
                seen[people] = True
                seen_people.add(people)
                people = self.favorite[people]

            if people in seen_people:
                count = len(seen_people)
                while start != people:
                    count -= 1
                    start = self.favorite[start]
                max_count = max(max_count, count)

        return max_count
