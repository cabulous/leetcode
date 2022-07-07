class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [True] * (len(s2) + 1)

        for i in range(1, len(s2) + 1):
            dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])

        return dp[-1]


# dfs
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        if s1_len + s2_len != s3_len:
            return False

        stack = [(0, 0)]
        visited = {(0, 0)}

        while stack:
            pt1, pt2 = stack.pop()
            if pt1 + pt2 == s3_len:
                return True
            if pt1 + 1 <= s1_len and s1[pt1] == s3[pt1 + pt2] and (pt1 + 1, pt2) not in visited:
                stack.append((pt1 + 1, pt2))
                visited.add((pt1 + 1, pt2))
            if pt2 + 1 <= s2_len and s2[pt2] == s3[pt1 + pt2] and (pt1, pt2 + 1) not in visited:
                stack.append((pt1, pt2 + 1))
                visited.add((pt1, pt2 + 1))

        return False


# https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        if s1_len + s2_len != s3_len:
            return False

        dp = [[True] * (s2_len + 1) for _ in range(s1_len + 1)]

        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, s2_len + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])

        return dp[-1][-1]
