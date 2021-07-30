from collections import Counter, defaultdict


# Prefix Hashmap
class MapSum:
    def __init__(self):
        self.map = {}
        self.score = Counter()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix: str) -> int:
        return self.score[prefix]


# Trie
class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.score = 0


class MapSum:
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for c in key:
            cur = cur.next[c]
            cur.score += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.next:
                return 0
            cur = cur.next[c]
        return cur.score
