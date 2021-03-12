# short
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = {s[i - k:i] for i in range(k, len(s) + 1)}
        return len(seen) == 1 << k


# rolling hash
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        seen = [False] * need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            if i >= k - 1 and seen[hash_val] is False:
                seen[hash_val] = True
                need -= 1
                if need == 0:
                    return True

        return False


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
