class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y
            return True
        return False


ALICE_TYPE = 1
BOB_TYPE = 2
BOTH_TYPE = 3


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice_uf = UnionFind(n + 1)
        bob_uf = UnionFind(n + 1)
        alice_edge = 0
        bob_edge = 0
        res = 0

        for edge_type, u, v in edges:
            if edge_type == BOTH_TYPE:
                if alice_uf.union(u, v):
                    bob_uf.union(u, v)
                    alice_edge += 1
                    bob_edge += 1
                else:
                    res += 1

        for edge_type, u, v in edges:
            if edge_type == ALICE_TYPE:
                if alice_uf.union(u, v):
                    alice_edge += 1
                else:
                    res += 1

        for edge_type, u, v in edges:
            if edge_type == BOB_TYPE:
                if bob_uf.union(u, v):
                    bob_edge += 1
                else:
                    res += 1

        return res if alice_edge == bob_edge == n - 1 else -1
