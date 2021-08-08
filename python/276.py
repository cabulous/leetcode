from functools import lru_cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(2000)
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        return total_ways(n)


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        total_ways = [0] * (n + 1)
        total_ways[1] = k
        total_ways[2] = k * k

        for i in range(3, n + 1):
            total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])

        return total_ways[-1]


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        two_posts_back = k
        one_post_back = k * k

        for i in range(3, n + 1):
            curr = (k - 1) * (one_post_back + two_posts_back)
            two_posts_back, one_post_back = one_post_back, curr

        return one_post_back
