# https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        path_len = {-1: 0}

        for line in input.splitlines():
            depth = line.count('\t')
            path_len[depth] = path_len[depth - 1] + len(line) - depth
            if line.count('.') > 0:
                res = max(res, path_len[depth] + depth)

        return res
