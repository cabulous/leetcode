class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        conversion_map = {}
        unique_char_str2 = set()

        for c1, c2 in zip(str1, str2):
            if c1 not in conversion_map:
                conversion_map[c1] = c2
                unique_char_str2.add(c2)
            elif conversion_map[c1] != c2:
                return False

        if len(unique_char_str2) < 26:
            return True

        return False
