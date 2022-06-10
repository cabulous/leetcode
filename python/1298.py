from typing import List


# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/discuss/462242/JavaC%2B%2BPython-Accumulate-LeeCode-Coins
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        opened_boxes = [i for i in boxes if status[i] == 1]

        for box in opened_boxes:
            for next_box in containedBoxes[box]:
                boxes.add(next_box)
                if status[next_box] == 1:
                    opened_boxes.append(next_box)
            for next_box in keys[box]:
                if status[next_box] == 0 and next_box in boxes:
                    opened_boxes.append(next_box)
                status[next_box] = 1

        return sum(candies[i] for i in opened_boxes)
