class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'

        s_vowels = []
        for ch in s:
            if ch in vowels:
                s_vowels.append(ch)

        res = []
        for ch in s:
            if ch in vowels:
                res.append(s_vowels.pop())
            else:
                res.append(ch)

        return ''.join(res)
