class UnionFind:

    def __init__(self, size=26):
        self.root = list(range(size))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if root_x < root_y:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for ch1, ch2 in zip(s1, s2):
            uf.union(self.hash(ch1), self.hash(ch2))

        res = []
        for ch in baseStr:
            ret = uf.find(self.hash(ch))
            res.append(chr(ret + ord('a')))

        return ''.join(res)

    def hash(self, ch):
        return ord(ch) - ord('a')
