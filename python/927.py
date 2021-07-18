from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total = sum(arr)
        if total % 3 != 0:
            return [-1, -1]

        ones = total / 3
        if ones == 0:
            return [0, len(arr) - 1]

        breaks = []
        sub_total = 0
        for i, x in enumerate(arr):
            if x == 1:
                sub_total += x
                if sub_total in {1, ones + 1, ones * 2 + 1}:
                    breaks.append(i)
                if sub_total in {ones, ones * 2, ones * 3}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        if not (arr[i1:j1 + 1] == arr[i2:j2 + 1] == arr[i3:j3 + 1]):
            return [-1, -1]

        zeros1 = i2 - j1 - 1
        zeros2 = i3 - j2 - 1
        zeros3 = len(arr) - j3 - 1

        if zeros1 < zeros3 or zeros2 < zeros3:
            return [-1, -1]

        j1 += zeros3
        j2 += zeros3

        return [j1, j2 + 1]
