from collections import defaultdict


# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/solutions/402401/python-use-topologically-sorted-items-and-groups-to-get-the-desired-order/
class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        group_count = m
        for node in range(len(group)):
            if group[node] == -1:
                group[node] = group_count
                group_count += 1

        graph_items = [[] for _ in range(n)]
        in_degree_items = [0] * n
        graph_groups = [[] for _ in range(group_count)]
        in_degree_groups = [0] * group_count
        for node in range(n):
            for prev_node in beforeItems[node]:
                graph_items[prev_node].append(node)
                in_degree_items[node] += 1
                if group[prev_node] != group[node]:
                    graph_groups[group[prev_node]].append(group[node])
                    in_degree_groups[group[node]] += 1

        item_order = self.get_top_order(graph_items, in_degree_items)
        group_order = self.get_top_order(graph_groups, in_degree_groups)
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
