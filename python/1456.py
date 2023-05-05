class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        left = 0
        curr = 0
        res = 0

        for right in range(len(s)):
            if right - left == k:
                if s[left] in vowels:
                    curr -= 1
                left += 1
            if s[right] in vowels:
                curr += 1
                res = max(res, curr)

        return res
