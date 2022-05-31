class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = {s[i - k:i] for i in range(k, len(s) + 1)}
        return len(seen) == 1 << k


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        seen = set()

        for i in range(k, len(s) + 1):
            tmp = s[i - k:i]
            if tmp not in seen:
                seen.add(tmp)
                need -= 1
                if need == 0:
                    return True

        return False
