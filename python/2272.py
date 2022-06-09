# https://leetcode.com/problems/substring-with-largest-variance/discuss/2038516/Python-Simple-Solution-Faster-than-100
class Solution:
    def largestVariance(self, s: str) -> int:
        chars = list(set(s))
        res = 0

        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                ch1 = chars[i]
                ch2 = chars[j]

                meet_ch1 = meet_ch2 = False

                diff = 0
                diff_max = diff_min = 0
                diff_last_ch1 = diff_last_ch2 = 0

                for ch in s:
                    if ch == ch1:
                        meet_ch1 = True
                        diff += 1
                        diff_max = max(diff_max, diff_last_ch1)
                        diff_last_ch1 = diff
                    elif ch == ch2:
                        meet_ch2 = True
                        diff -= 1
                        diff_min = min(diff_min, diff_last_ch2)
                        diff_last_ch2 = diff
                    else:
                        continue

                    if meet_ch1 and meet_ch2:
                        res = max(res, diff_max - diff, diff - diff_min)

        return res
