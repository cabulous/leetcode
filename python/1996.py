from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        res = 0
        curr_defence_max = 0
        for _, defence in properties:
            if defence < curr_defence_max:
                res += 1
            curr_defence_max = max(curr_defence_max, defence)

        return res
