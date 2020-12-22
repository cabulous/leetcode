# dfs
# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
class Solution:
    def partition(self, s: str) -> [[str]]:
        def dfs(sub_str, cur_list):
            if not sub_str:
                res.append(cur_list[:])
                return
            for i in range(1, len(sub_str) + 1):
                if sub_str[:i] == sub_str[i - 1::-1]:
                    cur_list.append(sub_str[:i])
                    dfs(sub_str[i:], cur_list)
                    cur_list.pop()

        res = []
        dfs(s, [])
        return res
