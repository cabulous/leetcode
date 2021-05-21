from typing import List


# Two Maps
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words))


# One Map
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            p = {}
            for x, y in zip(pattern, word):
                if p.setdefault(x, y) != y:
                    return False
            return len(set(p.values())) == len(p.values())

        return list(filter(match, words))


# https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m = {}
            return [m.setdefault(c, len(m)) for c in word]

        return [w for w in words if match(w) == match(pattern)]


# https://leetcode.com/problems/find-and-replace-pattern/discuss/161775/Short-python-isomorphism-solution
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        b = pattern

        def is_iso(a):
            return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))

        return list(filter(is_iso, words))
