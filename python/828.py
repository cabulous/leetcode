MOD = 10 ** 9 + 7


# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/423812/Python-detailed-explanation
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = [[-1, -1]] * 26
        dp = [0] * (len(s) + 1)

        for curr_index, char in enumerate(s):
            code = ord(char) - ord('A')
            first_index, second_index = index[code]
            dp[curr_index + 1] = dp[curr_index] + 1 + (curr_index - second_index - 1) - (second_index - first_index)
            index[code] = [second_index, curr_index]

        return sum(dp) % MOD
