class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        count_a = 0
        count_b = 0

        for i in range(len(s) // 2):
            if s[i] in vowels:
                count_a += 1
            if s[len(s) - 1 - i] in vowels:
                count_b += 1

        return count_a == count_b
