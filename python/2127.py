from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Python-Explanation-with-pictures.
class Solution:

    def __init__(self):
        self.favorite = []

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.favorite = favorite
        return max(self.count_in_loop(), self.count_in_pair())

    def count_in_pair(self):
        seen = [False] * len(self.favorite)
        pair = []

        for i in range(len(self.favorite)):
            if self.favorite[self.favorite[i]] == i and not seen[i]:
                pair.append([i, self.favorite[i]])
                seen[i] = True
                seen[self.favorite[i]] = True

        graph = defaultdict(list)
        for i in range(len(self.favorite)):
            graph[self.favorite[i]].append(i)

        res = 0
        for a, b in pair:
            arm_a = self.arm_length(graph, a, b)
            arm_b = self.arm_length(graph, b, a)
            res += 2 + arm_a + arm_b

        return res

    def arm_length(self, graph, start, exclude):
        queue = deque()

        for cand in graph[start]:
            if cand != exclude:
                queue.append([cand, 1])

        res = 0
        while queue:
            people, count = queue.popleft()
            res = max(res, count)
            for next_people in graph[people]:
                queue.append([next_people, count + 1])

        return res

    def count_in_loop(self):
        seen = [False] * len(self.favorite)
        res = 0

        for i in range(len(self.favorite)):
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
                res = max(res, count)

        return res
