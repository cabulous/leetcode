from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        prefix_sum = 0
        prefix_sum_acc = [0]
        stack = [-1]
        res = 0
        strength += [0]

        for right, num in enumerate(strength):
            prefix_sum += num
            prefix_sum_acc.append(prefix_sum + prefix_sum_acc[-1])

            while stack and num < strength[stack[-1]]:
                min_index = stack.pop()
                left = stack[-1]

                prefix_sum_left = prefix_sum_acc[min_index] - prefix_sum_acc[max(left, 0)]
                prefix_sum_right = prefix_sum_acc[right] - prefix_sum_acc[min_index]

                dist_left = min_index - left
                dist_right = right - min_index

                res += strength[min_index] * (prefix_sum_right * dist_left - prefix_sum_left * dist_right) % MOD

            stack.append(right)

        return res % MOD
