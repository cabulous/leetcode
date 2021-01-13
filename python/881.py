from typing import List


# https://leetcode.com/problems/boats-to-save-people/discuss/156740/C%2B%2BJavaPython-Two-Pointers
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 1
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
