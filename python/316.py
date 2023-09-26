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
