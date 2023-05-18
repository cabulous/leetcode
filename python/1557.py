class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        in_degrees = set(v for u, v in edges)
        all_nodes = set(range(n))
        return list(all_nodes - in_degrees)
