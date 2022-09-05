from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [arr[-1]]
        curr = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            curr = max(curr, arr[i])
            res.append(curr)
        return list(reversed(res[:-1])) + [-1]
