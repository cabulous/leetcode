import bisect


class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        k, r = divmod(n, 2)
        mid = num[k] if r else ''

        if k > 1:
            s = num[:k]
            stack = []
            for i in range(k - 1, -1, -1):
                if not stack or s[i] >= s[i + 1]:
                    stack.append(s[i])
                else:
                    index = bisect.bisect_right(stack, s[i])
                    x = stack[index]
                    stack[index] = s[i]
                    half = s[:i] + x + ''.join(stack)
                    return half + mid + half[::-1]

        return ''
