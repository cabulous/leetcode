# https://leetcode.com/problems/cracking-the-safe/discuss/110266/A-Brainstorming-Python-Solution
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        res = '0' * (n - 1)

        for _ in range(k ** n):
            curr = res[-n + 1:] if n > 1 else ''
            for digit in reversed(range(k)):
                candidate = curr + str(digit)
                if candidate not in visited:
                    visited.add(candidate)
                    res += str(digit)
                    break

        return res
