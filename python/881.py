from typing import List


# https://leetcode.com/problems/boats-to-save-people/discuss/156740/C%2B%2BJavaPython-Two-Pointers
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1

        return left
