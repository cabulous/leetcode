# https://leetcode.com/problems/combinations/solutions/3845249/iterative-backtracking-video-100-efficient-combinatorial-generation/
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [list(comb) for comb in self.helper(range(1, n + 1), k)]

    def helper(self, elems, k):
        if k > len(elems):
            return

        elems_tuple = tuple(elems)
        curr_indices = list(range(k))

        while True:
            yield tuple(elems_tuple[i] for i in curr_indices)
            for i in reversed(range(k)):
                if curr_indices[i] != i + len(elems_tuple) - k:
                    break
            else:
                return
            curr_indices[i] += 1
            for j in range(i + 1, k):
                curr_indices[j] = curr_indices[j - 1] + 1
