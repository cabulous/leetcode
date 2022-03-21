from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ''

        count = Counter(s)
        min_index = 0

        for i, ch in enumerate(s):
            if ch < s[min_index]:
                min_index = i
            count[ch] -= 1
            if count[ch] == 0:
                break

        remaining = s[min_index:].replace(s[min_index], '')

        return s[min_index] + self.removeDuplicateLetters(remaining)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last = {ch: i for i, ch in enumerate(s)}

        for i, ch in enumerate(s):
            if ch not in seen:
                while stack and ch < stack[-1] and i < last[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(ch)
                stack.append(ch)

        return ''.join(stack)
