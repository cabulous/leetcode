from collections import defaultdict, Counter


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = Counter()
        for t, s in prerequisites:
            graph[s].append(t)
            in_degree[t] += 1

        zero_degree = [i for i in range(numCourses) if in_degree[i] == 0]

        for node in zero_degree:
            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    zero_degree.append(next_node)

        return len(zero_degree) == numCourses
