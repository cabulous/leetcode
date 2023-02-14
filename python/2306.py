class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        initial_group = [set() for _ in range(26)]
        for idea in ideas:
            initial_group[ord(idea[0]) - ord('a')].add(idea[1:])

        res = 0
        for i in range(25):
            for j in range(i + 1, 26):
                mutual = len(initial_group[i] & initial_group[j])
                res += 2 * (len(initial_group[i]) - mutual) * (len(initial_group[j]) - mutual)

        return res
