from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        prefix_sum = 0
        stack = [-1]
        acc = [0]
        res = 0
        strength += [0]

        for right, num in enumerate(strength):
            prefix_sum += num
            acc.append(prefix_sum + acc[-1])

            while stack and strength[stack[-1]] > num:
                index = stack.pop()
                left = stack[-1]

                acc_left = acc[index] - acc[max(left, 0)]
                acc_right = acc[right] - acc[index]

                dist_left = index - left
                dist_right = right - index

                res += strength[index] * (acc_right * dist_left - acc_left * dist_right) % MOD

            stack.append(right)

        return res % MOD
