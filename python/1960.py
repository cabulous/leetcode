from itertools import accumulate


# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/Python-O(n)-with-Manacher-explained
class Solution:
    def maxProduct(self, s: str) -> int:
        t1 = self.helper(s)
        t2 = self.helper(s[::-1])[::-1][1:] + [0]

        return max(x * y for x, y in zip(t1, t2))

    def manachers(self, s):
        a = '@#' + '#'.join(s) + '#$'
        z = [0] * len(a)
        center = right = 0

        for i in range(1, len(a) - 1):
            if i < right:
                z[i] = min(right - i, z[2 * center - i])
            while a[i + z[i] + 1] == a[i - z[i] - 1]:
                z[i] += 1
            if i + z[i] > right:
                center = i
                right = i + z[i]

        return z[2:-2:2]

    def helper(self, s):
        man = self.manachers(s)
        n = len(s)
        ints = [(i - man[i] // 2, i + man[i] // 2) for i in range(n)]
        arr = [0] * n

        for a, b in ints:
            arr[b] = max(arr[b], b - a + 1)

        for i in range(n - 2, -1, -1):
            arr[i] = max(arr[i], arr[i + 1] - 2)

        return list(accumulate(arr, max))
