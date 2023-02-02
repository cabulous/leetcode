class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        lookup = {ch: idx for idx, ch in enumerate(order)}
        words_idx = [[lookup[ch] for ch in w] for w in words]
        return all(idx1 <= idx2 for idx1, idx2 in zip(words_idx, words_idx[1:]))
