# Implementation of Python Function lower
class Solution:
    def toLowerCase(self, s: str) -> str:
        is_upper = lambda x: 'A' <= x <= 'Z'
        to_lower = lambda x: chr(ord(x) | 32)

        return ''.join([to_lower(x) if is_upper(x) else x for x in s])


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution:
    def toLowerCase(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))

        return ''.join([h[x] if x in h else x for x in s])
