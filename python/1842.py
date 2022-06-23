import bisect


class Solution:
    def nextPalindrome(self, num: str) -> str:
        half_idx, remainder = divmod(len(num), 2)
        if half_idx <= 1:
            return ''

        mid = num[half_idx] if remainder == 1 else ''
        half = num[:half_idx]
        stack = []

        for i in range(half_idx - 1, -1, -1):
            if not stack or half[i] >= half[i + 1]:
                stack.append(half[i])
            else:
                index = bisect.bisect_right(stack, half[i])
                pivot = stack[index]
                stack[index] = half[i]
                greater_half = half[:i] + pivot + ''.join(stack)
                return greater_half + mid + greater_half[::-1]

        return ''
