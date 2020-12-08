from collections import deque


def find_circle_num_bfs(self, M) -> int:
    if not M or not M[0]:
        return 0

    m = len(M)
    visited = [0] * m
    queue = deque()
    count = 0

    for i in range(m):
        if visited[i] == 0:
            queue.append(i)
            while queue:
                cur = queue.popleft()
                visited[cur] = 1
                for j in range(i, m):
                    if M[cur][j] == 1 and visited[j] == 0:
                        queue.append(j)
            count += 1
    return count


def find_circle_num_dfs(self, M) -> int:
    if not M or not M[0]:
        return 0

    def dfs(i):
        for j in range(m):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                dfs(j)

    m = len(M)
    visited = [0] * m
    count = 0

    for i in range(m):
        if visited[i] == 0:
            dfs(i)
            count += 1

    return count


def find_circle_num_union_and_find(self, M) -> int:
    if not M or not M[0]:
        return 0

    def find(x):
        if uf[x] == x:
            return uf[x]
        return find(uf[x])

    m = len(M)
    uf = {i: i for i in range(m)}

    for i in range(m):
        for j in range(i + 1, m):
            if M[i][j] == 1:
                uf[find(i)] = find(j)

    return sum([1 for k, v in uf.items() if k == v])