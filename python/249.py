from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strings:
            hash_key = self.get_hash(string)
            groups[hash_key].append(string)

        return list(groups.values())

    def shift_letter(self, letter, shift):
        return chr((ord(letter) - shift) % 26 + ord('a'))

    def get_hash(self, string):
        shift = ord(string[0])
        return ''.join(self.shift_letter(letter, shift) for letter in string)


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strings:
            hash_key = self.get_hash(string)
            groups[hash_key].append(string)

        return list(groups.values())

    def get_hash(self, string):
        key = []
        for a, b in zip(string, string[1:]):
            key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
        return ''.join(key)
