import bisect


class Solution:
    def nextPalindrome(self, num: str) -> str:
        half_idx, rem = divmod(len(num), 2)
        if half_idx <= 1:
            return ''

        half = num[:half_idx]
        stack = []

        for i in range(half_idx - 1, -1, -1):
            if not stack or half[i] >= half[i + 1]:
                stack.append(half[i])
            else:
                index = bisect.bisect_right(stack, half[i])
                pivot_val = stack[index]
                stack[index] = half[i]
                greater_half = half[:i] + pivot_val + ''.join(stack)
                mid = num[half_idx] if rem == 1 else ''
                return greater_half + mid + greater_half[::-1]

        return ''
