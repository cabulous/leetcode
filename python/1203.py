from collections import defaultdict


# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/solutions/402401/python-use-topologically-sorted-items-and-groups-to-get-the-desired-order/
class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        group_count = m
        for node in range(len(group)):
            if group[node] == -1:
                group[node] = group_count
                group_count += 1

        item_graph = [[] for _ in range(n)]
        item_in_degree = [0] * n
        group_graph = [[] for _ in range(group_count)]
        group_in_degree = [0] * group_count
        for node in range(n):
            for prev_node in beforeItems[node]:
                item_graph[prev_node].append(node)
                item_in_degree[node] += 1
                if group[prev_node] != group[node]:
                    group_graph[group[prev_node]].append(group[node])
                    group_in_degree[group[node]] += 1

        item_order = self.get_top_order(item_graph, item_in_degree)
        group_order = self.get_top_order(group_graph, group_in_degree)
        if not item_order or not group_order:
            return []

        order_within_group = defaultdict(list)
        for node in item_order:
            order_within_group[group[node]].append(node)

        res = []
        for group in group_order:
            res += order_within_group[group]

        return res

    def get_top_order(self, graph, in_degree):
        res = []
        stack = [node for node in range(len(graph)) if in_degree[node] == 0]
        while stack:
            node = stack.pop()
            res.append(node)
            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    stack.append(next_node)
        return res if len(res) == len(graph) else []
