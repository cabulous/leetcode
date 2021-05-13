import itertools
from typing import List


# https://leetcode.com/problems/ambiguous-coordinates/discuss/123851/C%2B%2BJavaPython-Solution-with-Explanation
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def find(s):
            if not s or (len(s) > 1 and s[0] == s[-1] == '0'):
                return []
            if s[-1] == '0':
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            return [s] + [s[:i] + '.' + s[i:] for i in range(1, len(s))]

        return ['(%s, %s)' % (a, b) for i in range(len(s)) for a, b in itertools.product(find(s[:i]), find(s[i:]))]


# Cartesian Product
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (not left.startswith('0') or left == '0') and (not right.endswith('0')):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]
        return ['({}, {})'.format(*cand)
                for i in range(1, len(s))
                for cand in itertools.product(make(s[:i]), make(s[i:]))]
