from functools import lru_cache

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/find-all-good-strings/discuss/555010/Python-Simple-DFS-with-KMP
def srange(a, b):
    yield from (chr(i) for i in range(ord(a), ord(b) + 1))


def failure(pattern):
    res = [0]
    i, target = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[target]:
            target += 1
            res += [target]
            i += 1
        elif target:
            target = res[target - 1]
        else:
            res += [0]
            i += 1
    return res


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        f = failure(evil)

        @lru_cache(None)
        def dfs(idx, max_matched=0, lb=True, rb=True):
            if max_matched == len(evil):
                return 0
            if idx == n:
                return 1

            left = s1[idx] if lb else 'a'
            right = s2[idx] if rb else 'z'
            candidates = [*srange(left, right)]

            res = 0
            for i, ch in enumerate(candidates):
                next_matched = max_matched
                while evil[next_matched] != ch and next_matched:
                    next_matched = f[next_matched - 1]
                res += dfs(
                    idx + 1,
                    next_matched + (ch == evil[next_matched]),
                    lb=(lb and i == 0),
                    rb=(rb and i == len(candidates) - 1)
                )

            return res

        return dfs(0) % MOD
