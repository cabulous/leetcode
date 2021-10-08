class Trie:
    def __init__(self):
        self.WORD_END = '#'
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t[self.WORD_END] = self.WORD_END

    def search_prefix(self, prefix: str):
        t = self.trie
        for w in prefix:
            if w not in t:
                return None
            t = t[w]
        return t

    def search(self, word: str) -> bool:
        t = self.search_prefix(word)
        if not t:
            return False
        return self.WORD_END in t

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None
