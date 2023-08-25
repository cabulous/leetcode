from collections import deque


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        queue = deque([(0, 0)])
        seen = {(0, 0)}
        while queue:
            pt1, pt2 = queue.popleft()
            if pt1 + pt2 == len(s3):
                return True
            if pt1 < len(s1) and s1[pt1] == s3[pt1 + pt2] and (pt1 + 1, pt2) not in seen:
                seen.add((pt1 + 1, pt2))
                queue.append((pt1 + 1, pt2))
            if pt2 < len(s2) and s2[pt2] == s3[pt1 + pt2] and (pt1, pt2 + 1) not in seen:
                seen.add((pt1, pt2 + 1))
                queue.append((pt1, pt2 + 1))

        return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [True] * (len(s2) + 1)

        for pt2 in range(len(s2)):
            dp[pt2 + 1] = dp[pt2] and s2[pt2] == s3[pt2]

        for pt1 in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[pt1 - 1] == s3[pt1 - 1]
            for pt2 in range(1, len(s2) + 1):
                dp[pt2] = (
                        dp[pt2] and s1[pt1 - 1] == s3[pt1 - 1 + pt2]
                        or dp[pt2 - 1] and s2[pt2 - 1] == s3[pt1 - 1 + pt2]
                )

        return dp[-1]
