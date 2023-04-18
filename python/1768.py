class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        read_idx = 0
        res = []

        while read_idx < len(word1) and read_idx < len(word2):
            res.append(word1[read_idx])
            res.append(word2[read_idx])
            read_idx += 1

        return ''.join(res) + word1[read_idx:] + word2[read_idx:]
