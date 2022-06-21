from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Python-Explanation-with-pictures.
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        max_count = 0
        seen = [False] * n

        for i in range(n):
            if not seen[i]:
                start = i
                curr_people = i
                curr_set = set()

                while not seen[curr_people]:
                    seen[curr_people] = True
                    curr_set.add(curr_people)
                    curr_people = favorite[curr_people]

                if curr_people in curr_set:
                    curr_count = len(curr_set)
                    while start != curr_people:
                        curr_count -= 1
                        start = favorite[start]
                    max_count = max(max_count, curr_count)

        pair = []
        visited = [False] * n
        for i in range(n):
            if favorite[favorite[i]] == i and not visited[i]:
                pair.append([i, favorite[i]])
                visited[i] = True
                visited[favorite[i]] = True

        child = defaultdict(list)
        for i in range(n):
            child[favorite[i]].append(i)

        res = 0
        for a, b in pair:
            max_arm_a = 0
            queue_a = deque()
            for cand in child[a]:
                if cand != b:
                    queue_a.append([cand, 1])
            while queue_a:
                people, count = queue_a.popleft()
                max_arm_a = max(max_arm_a, count)
                for next_people in child[people]:
                    queue_a.append([next_people, count + 1])

            max_arm_b = 0
            queue_b = deque()
            for cand in child[b]:
                if cand != a:
                    queue_b.append([cand, 1])
            while queue_b:
                people, count = queue_b.popleft()
                max_arm_b = max(max_arm_b, count)
                for next_people in child[people]:
                    queue_b.append([next_people, count + 1])

            res += 2 + max_arm_a + max_arm_b

        return max(max_count, res)
