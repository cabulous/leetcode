from typing import List
from collections import Counter


# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/discuss/390392/Python-Binary-Search
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for target in mat[0]:
            found = True
            for row in mat[1:]:
                if not self.binary_search(row, target):
                    found = False
                    break
            if found:
                return target

        return -1

    def binary_search(self, arr, target):
        if not arr:
            return False
        if target < arr[0]:
            return False
        if arr[-1] < target:
            return False

        lo = 0
        hi = len(arr)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if arr[mi] == target:
                return True
            if arr[mi] < target:
                lo = mi + 1
            else:
                hi = mi

        return False


# simple but cannot handle duplicates
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/discuss/387092/JavaC%2B%2BPython-Brute-Force-Count
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = Counter()
        target_counts = len(mat)

        for row in mat:
            for num in row:
                count[num] += 1
                if count[num] == target_counts:
                    return num

        return -1
