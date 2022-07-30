from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        res = []
        for num in arr2:
            res += [num] * count[num]
            count[num] = 0

        remain = [(num, count) for num, count in count.items() if count > 0]
        for num, num_count in sorted(remain):
            res += [num] * num_count

        return res
