class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        steps = [0] * len(edges)
        curr_step = 1
        res = -1

        for node in range(len(edges)):
            if steps[node] > 0:
                continue
            start_step = curr_step
            curr_node = node
            while curr_node != -1 and steps[curr_node] == 0:
                steps[curr_node] = curr_step
                curr_step += 1
                curr_node = edges[curr_node]
            if curr_node != -1 and steps[curr_node] >= start_step:
                res = max(res, curr_step - steps[curr_node])

        return res
