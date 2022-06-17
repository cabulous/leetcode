from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2061985/JavaC%2B%2BPython-One-Pass-Solution
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
                pivot_index = stack.pop()
                left = stack[-1]

                prefix_sum_left = prefix_sum_acc[pivot_index] - prefix_sum_acc[max(0, left)]
                prefix_sum_right = prefix_sum_acc[right] - prefix_sum_acc[pivot_index]

                dist_left = pivot_index - left
                dist_right = right - pivot_index

                res += strength[pivot_index] * (prefix_sum_right * dist_left - prefix_sum_left * dist_right) % MOD

            stack.append(right)

        return res % MOD
