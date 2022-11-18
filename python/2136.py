from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curr_plant_time = 0
        res = 0

        sorted_flowers = sorted(range(len(growTime)), key=lambda x: -growTime[x])

        for flower in sorted_flowers:
            curr_plant_time += plantTime[flower]
            res = max(res, curr_plant_time + growTime[flower])

        return res
