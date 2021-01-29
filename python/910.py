# https://leetcode.com/problems/smallest-range-ii/discuss/173377/C%2B%2BJavaPython-Add-0-or-2-*-K
class Solution:
    def smallestRangeII(self, A: [int], K: int) -> int:
        A.sort()
        if A[-1] - A[0] >= 4 * K:
            return A[-1] - A[0] - 2 * K
        if A[-1] - A[0] <= K:
            return A[-1] - A[0]
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[-1], A[i] + 2 * K)
            small = min(A[i + 1], A[0] + 2 * K)
            res = min(res, big - small)
        return res


# improve
class Solution:
    def smallestRangeII(self, A: [int], K: int) -> int:
        ma, mi = max(A), min(A)
        if ma - mi >= 4 * K:
            return ma - mi - 2 * K
        if ma - mi <= K:
            return ma - mi
        inter = sorted([i for i in A if ma - 2 * K < i < mi + 2 * K] + [ma - 2 * K, mi + 2 * K])
        return min(a + 2 * K - b for a, b in zip(inter, inter[1:]))
