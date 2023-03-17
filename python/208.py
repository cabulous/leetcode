class Trie:

    def __init__(self):
        self.root = {}
        self.WORD_END = '#'

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.WORD_END] = word

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        if not node:
            return False
        return self.WORD_END in node

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None
