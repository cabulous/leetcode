# bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]
        visited = {0}
        step = 0

        while curs:
            nex = []
            for node in curs:
                if node == n - 1:
                    return step
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)
            curs = nex
            step += 1

        return -1


# bidirectional bfs
class Solution:
    def minJumps(self, arr: [int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]
        other = [n - 1]
        visited = {0, n - 1}
        step = 0

        while curs:
            if len(curs) > len(other):
                curs, other = other, curs
            nex = []
            for node in curs:
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)
            curs = nex
            step += 1

        return -1
