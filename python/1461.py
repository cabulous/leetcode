class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set(s[i - k:i] for i in range(k, len(s) + 1))
        return len(seen) == 1 << k


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        seen = set()

        for i in range(k, len(s) + 1):
            curr = s[i - k:i]
            if curr not in seen:
                seen.add(curr)
                need -= 1
                if need == 0:
                    return True

        return False
