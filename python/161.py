class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)
        if nt - ns > 1 or s == t:
            return False
        for i in range(ns):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]
        return True
