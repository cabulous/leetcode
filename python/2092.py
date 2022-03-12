from collections import defaultdict, deque
from itertools import groupby
from typing import List


# https://leetcode.com/problems/find-all-people-with-secret/discuss/1599870/Python3-BFS-or-DFS-by-group
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        groups = groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2])
        res = {0, firstPerson}

        for _, group in groups:
            queue = set()
            graph = defaultdict(list)

            for person1, person2, _ in group:
                graph[person1].append(person2)
                graph[person2].append(person1)
                if person1 in res:
                    queue.add(person1)
                if person2 in res:
                    queue.add(person2)

            queue = deque(queue)

            while queue:
                person = queue.popleft()
                for next_person in graph[person]:
                    if next_person not in res:
                        res.add(next_person)
                        queue.append(next_person)

        return res
