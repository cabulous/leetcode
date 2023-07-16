# https://leetcode.com/problems/smallest-sufficient-team/solutions/334572/java-c-python-dp-solution/
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_idx = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}

        for i, p in enumerate(people):
            curr_skill = 0
            for skill in p:
                if skill in skill_idx:
                    curr_skill |= 1 << skill_idx[skill]
            for prev, need in dp.copy().items():
                comb = curr_skill | prev
                if comb == prev:
                    continue
                if comb not in dp or len(dp[comb]) > len(need) + 1:
                    dp[comb] = need + [i]

        return dp[(1 << len(req_skills)) - 1]
