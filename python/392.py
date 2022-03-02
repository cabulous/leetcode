class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = t_index = 0
        while s_index < len(t) and t_index < len(s):
            if t[s_index] == s[t_index]:
                t_index += 1
            s_index += 1
        return t_index == len(s)
