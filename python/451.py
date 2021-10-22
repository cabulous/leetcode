from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        str_builder = []

        for letter, freq in counts.most_common():
            str_builder.append(letter * freq)

        return ''.join(str_builder)
