class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        lookup = {}
        for i in range(len(words)):
            char = pattern[i]
            word = words[i]

            char_key = f'char_{char}'
            word_key = f'word_{word}'

            if char_key not in lookup:
                lookup[char_key] = i
            if word_key not in lookup:
                lookup[word_key] = i

            if lookup[char_key] != lookup[word_key]:
                return False

        return True
