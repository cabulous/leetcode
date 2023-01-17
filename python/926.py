class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix_sum = [0]
        for digit in s:
            prefix_sum.append(prefix_sum[-1] + int(digit))

        res = len(s)
        for i in range(len(prefix_sum)):
            flip_to_zero = prefix_sum[i]
            flip_to_one = (len(s) - i) - (prefix_sum[-1] - prefix_sum[i])
            res = min(res, flip_to_zero + flip_to_one)

        return res
