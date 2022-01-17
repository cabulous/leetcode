class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            char = pattern[i]
            word = words[i]

            char_key = f'char_{char}'
            word_key = f'word_{word}'

            if char_key not in map_index:
                map_index[char_key] = i

            if word_key not in map_index:
                map_index[word_key] = i

            if map_index[char_key] != map_index[word_key]:
                return False

        return True
