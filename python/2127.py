from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Python-Explanation-with-pictures.
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
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
                people = favorite[people]

            if people in seen_people:
                count = len(seen_people)
                while start != people:
                    count -= 1
                    start = favorite[start]
                max_count = max(max_count, count)

        pair = []
        visited = [False] * n
        for i in range(n):
            if favorite[favorite[i]] == i and not visited[i]:
                pair.append([i, favorite[i]])
                visited[i] = True
                visited[favorite[i]] = True

        graph = defaultdict(list)
        for i in range(n):
            graph[favorite[i]].append(i)

        res = 0
        for a, b in pair:
            max_arm_a = self.arm_length(graph, a, b)
            max_arm_b = self.arm_length(graph, b, a)
            res += 2 + max_arm_a + max_arm_b

        return max(max_count, res)

    def arm_length(self, graph, start, exclude):
        max_arm = 0
        queue = deque()

        for cand in graph[start]:
            if cand != exclude:
                queue.append([cand, 1])

        while queue:
            people, count = queue.popleft()
            max_arm = max(max_arm, count)
            for next_people in graph[people]:
                queue.append([next_people, count + 1])

        return max_arm
