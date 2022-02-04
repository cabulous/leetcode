class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        map_index = {}
        for index in range(len(words)):
            char = pattern[index]
            word = words[index]

            char_key = f'char_{char}'
            word_key = f'word_{word}'

            if char_key not in map_index:
                map_index[char_key] = index
            if word_key not in map_index:
                map_index[word_key] = index

            if map_index[char_key] != map_index[word_key]:
                return False

        return True
