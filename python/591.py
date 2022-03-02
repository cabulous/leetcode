# https://leetcode.com/problems/tag-validator/discuss/279586/Python-One-pass-leveraging-State-Machine
class Solution:
    def isValid(self, code: str) -> bool:
        state = ['plain', 'open', 'close', 'cdata']
        curr = 'plain'

        open_tag = []
        close_tag = []

        stack = []
        i = 0

        while i < len(code):
            ch = code[i]

            if curr == 'plain':
                if not stack and i != 0:
                    return False

                if code[i:i + 9] == '<![CDATA[':
                    curr = 'cdata'
                    i += 9
                    continue
                elif code[i:i + 2] == '</':
                    curr = 'close'
                    i += 2
                    continue
                elif ch == '<':
                    curr = 'open'

            elif curr == 'open':
                if ch == '>':
                    if len(open_tag) < 1 or 9 < len(open_tag):
                        return False
                    stack.append(''.join(open_tag))
                    open_tag = []
                    curr = 'plain'
                    i += 1
                    continue

                if not ch.isupper():
                    return False

                open_tag.append(ch)

            elif curr == 'close':
                if ch == '>':
                    if len(close_tag) < 1 or 9 < len(close_tag):
                        return False

                    close_tag_str = ''.join(close_tag)
                    if not stack or close_tag_str != stack[-1]:
                        return False
                    stack.pop()

                    close_tag = []
                    curr = 'plain'
                    i += 1
                    continue

                if not ch.isupper():
                    return False

                close_tag.append(ch)

            elif curr == 'cdata':
                if code[i:i + 3] == ']]>':
                    curr = 'plain'
                    i += 3
                    continue

            i += 1

        if stack or curr != 'plain':
            return False

        return True
