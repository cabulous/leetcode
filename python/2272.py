# https://leetcode.com/problems/substring-with-largest-variance/discuss/2038516/Python-Simple-Solution-Faster-than-100
class Solution:
    def largestVariance(self, s: str) -> int:
        chars = list(set(s))
        res = 0

        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                ch1 = chars[i]
                ch2 = chars[j]

                diff = 0
                max_diff = min_diff = 0
                last_ch1_diff = last_ch2_diff = 0

                meet_ch1 = meet_ch2 = False

                for ch in s:
                    if ch == ch1:
                        meet_ch1 = True
                        max_diff = max(max_diff, last_ch1_diff)
                        diff += 1
                        last_ch1_diff = diff
                    elif ch == ch2:
                        meet_ch2 = True
                        min_diff = min(min_diff, last_ch2_diff)
                        diff -= 1
                        last_ch2_diff = diff
                    else:
                        continue

                    if meet_ch1 and meet_ch2:
                        res = max(res, max_diff - diff, diff - min_diff)

        return res
