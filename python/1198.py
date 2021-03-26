from typing import List
from collections import Counter


# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/discuss/390392/Python-Binary-Search
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return -1

        for target in mat[0]:
            flag = True
            for row in mat[1:]:
                if not self.binary_search(row, target):
                    flag = False
                    break
            if flag:
                return target

        return -1

    def binary_search(self, arr, target):
        if arr and arr[0] > target:
            return False
        if arr and arr[-1] < target:
            return False
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] == target:
                return True
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False


# simple but cannot handle duplicates
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/discuss/387092/JavaC%2B%2BPython-Brute-Force-Count
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c = Counter()
        n = len(mat)
        for row in mat:
            for a in row:
                c[a] += 1
                if c[a] == n:
                    return a
        return -1
