import itertools
from typing import List
from collections import Counter


# https://leetcode.com/problems/3sum-with-multiplicity/discuss/181131/C%2B%2BJavaPython-O(N-%2B-101-*-101)
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        c = Counter(arr)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
            elif i == j != k:
                res += c[i] * (c[i] - 1) / 2 * c[k]
            elif i < k and j < k:
                res += c[i] * c[j] * c[k]
        return int(res % mod)


# 3 pointer
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        res = 0
        arr.sort()

        for i, x in enumerate(arr):
            t = target - arr[i]
            j, k = i + 1, len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < t:
                    j += 1
                elif arr[j] + arr[k] > t:
                    k -= 1
                elif arr[j] != arr[k]:
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        right += 1
                        k -= 1
                    res += left * right
                    res %= mod
                    j += 1
                    k -= 1
                else:
                    res += (k - j + 1) * (k - j) / 2
                    res %= mod
                    break

        return int(res)
