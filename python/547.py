class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))
        self.group = size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.group -= 1
            self.root[root_x] = root_y


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.group
