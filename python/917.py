class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []

        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)

        return ''.join(ans)


# https://leetcode.com/problems/reverse-only-letters/discuss/178419/JavaC%2B%2BPython-Two-Pointers-One-pass
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        i, j = 0, len(ans) - 1

        while i < j:
            if not ans[i].isalpha():
                i += 1
            elif not ans[j].isalpha():
                j -= 1
            else:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1

        return ''.join(ans)
