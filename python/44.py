class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == s or set(p) == {'*'}:
            return True

        if p == '' or s == '':
            return False

        s_len, p_len = len(s), len(p)
        dp = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        dp[0][0] = True

        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1
                while not dp[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                dp[p_idx][s_idx - 1] = dp[p_idx - 1][s_idx - 1]
                while s_idx < s_len + 1:
                    dp[p_idx][s_idx] = True
                    s_idx += 1

            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1]

            else:
                for s_idx in range(1, s_len + 1):
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]

        return dp[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1

            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1

            elif star_idx == -1:
                return False

            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        return all(p[i] == '*' for i in range(p_idx, p_len))
