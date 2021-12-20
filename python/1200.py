from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        res = []

        for i in range(len(arr) - 1):
            curr_diff = arr[i + 1] - arr[i]
            if curr_diff == min_diff:
                res.append([arr[i], arr[i + 1]])
            elif curr_diff < min_diff:
                res = [[arr[i], arr[i + 1]]]
                min_diff = curr_diff

        return res


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_el, max_el = min(arr), max(arr)
        shift = -min_el
        line = [0] * (max_el - min_el + 1)
        res = []

        for num in arr:
            line[num + shift] = 1

        min_diff = max_el - min_el
        prev = 0

        for curr in range(1, max_el + shift + 1):
            if line[curr] == 0:
                continue
            if curr - prev == min_diff:
                res.append([prev - shift, curr - shift])
            elif curr - prev < min_diff:
                res = [[prev - shift, curr - shift]]
                min_diff = curr - prev
            prev = curr

        return res
