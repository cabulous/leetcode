# dfs
# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution:
    def partition(self, s: str) -> [[str]]:
        def dfs(cur, path):
            if not cur:
                res.append(path[:])
                return
            for i in range(1, len(cur) + 1):
                if cur[:i] == cur[i - 1::-1]:
                    path.append(cur[:i])
                    dfs(cur[i:], path)
                    path.pop()

        res = []
        dfs(s, [])
        return res

