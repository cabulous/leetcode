from collections import defaultdict, deque


# bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        graph = defaultdict(list)
        for idx, val in enumerate(arr):
            graph[val].append(idx)

        queue = deque([0])
        visited = {0}
        step = 0
        target = len(arr) - 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return step

                for next_node in graph[arr[node]]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
                graph[arr[node]].clear()

                for next_node in (node - 1, node + 1):
                    if 0 <= next_node < len(arr) and next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)

            step += 1

        return -1


# bidirectional bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        if len(arr) <= 1:
            return 0

        graph = defaultdict(list)
        for idx, val in enumerate(arr):
            graph[val].append(idx)

        curr = deque([0])
        other = deque([len(arr) - 1])
        visited = {0, len(arr) - 1}
        step = 0

        while curr:
            if len(curr) > len(other):
                curr, other = other, curr

            for _ in range(len(curr)):
                node = curr.popleft()

                for next_node in graph[arr[node]]:
                    if next_node in other:
                        return step + 1
                    if next_node not in visited:
                        visited.add(next_node)
                        curr.append(next_node)
                graph[arr[node]].clear()

                for next_node in (node - 1, node + 1):
                    if next_node in other:
                        return step + 1
                    if 0 <= next_node < len(arr) and next_node not in visited:
                        visited.add(next_node)
                        curr.append(next_node)

            step += 1

        return -1
