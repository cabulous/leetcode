# https://leetcode.com/problems/reducing-dishes/solutions/563384/java-c-python-easy-and-concise/?orderBy=most_votes
class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        curr = 0
        res = 0

        dishes = sorted(satisfaction)
        while dishes and dishes[-1] + curr > 0:
            curr += dishes.pop()
            res += curr

        return res
