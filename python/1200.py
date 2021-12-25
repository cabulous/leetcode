from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        res = []

        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i - 1]
            if curr_diff == min_diff:
                res.append([arr[i - 1], arr[i]])
            elif curr_diff < min_diff:
                min_diff = curr_diff
                res = [[arr[i - 1], arr[i]]]

        return res
