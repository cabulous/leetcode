# Implementation of Python Function lower
class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(self.to_lower(x) if self.is_upper(x) else x for x in s)

    def is_upper(self, x):
        return 'A' <= x <= 'Z'

    def to_lower(self, x):
        return chr(ord(x) | 32)


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution:
    def toLowerCase(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))

        return ''.join([h[x] if x in h else x for x in s])
