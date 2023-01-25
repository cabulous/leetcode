from typing import List


# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/solutions/3095880/easy-solution-fully-explained-two-dfs-c-python3-commented/
class Solution:

    def __init__(self):
        self.edges = []

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.edges = edges

        dist1 = [-1] * len(edges)
        self.dfs(node1, dist1, 0)

        dist2 = [-1] * len(edges)
        self.dfs(node2, dist2, 0)

        min_dist = float('inf')
        res = -1
        for i in range(len(edges)):
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                res = i

        return res

    def dfs(self, node, dist, steps):
        while node != -1 and dist[node] == -1:
            dist[node] = steps
            steps += 1
            node = self.edges[node]
