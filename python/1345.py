from collections import defaultdict


# bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)

        cur = [0]
        visited = {0}
        step = 0

        while cur:
            nxt = []
            for node in cur:
                if node == n - 1:
                    return step
                for next_node in graph[arr[node]]:
                    if next_node not in visited:
                        visited.add(next_node)
                        nxt.append(next_node)
                graph[arr[node]].clear()
                for next_node in [node - 1, node + 1]:
                    if 0 <= next_node < n and next_node not in visited:
                        visited.add(next_node)
                        nxt.append(next_node)
            step += 1
            cur = nxt

        return -1


# bidirectional bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)

        cur = [0]
        other = [n - 1]
        visited = {0, n - 1}
        step = 0

        while cur:
            if len(cur) > len(other):
                cur, other = other, cur
            nxt = []
            for node in cur:
                for next_node in graph[arr[node]]:
                    if next_node in other:
                        return step + 1
                    if next_node not in visited:
                        visited.add(next_node)
                        nxt.append(next_node)
                graph[arr[node]].clear()
                for next_node in [node - 1, node + 1]:
                    if next_node in other:
                        return step + 1
                    if 0 <= next_node < n and next_node not in visited:
                        visited.add(next_node)
                        nxt.append(next_node)
            step += 1
            cur = nxt

        return -1
