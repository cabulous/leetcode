from collections import defaultdict, deque


# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/59725/Python-easy-to-follow-solution-using-Trie./507243
class TrieNode:

    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.next[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        queue = deque([(self.root, 0)])
        while queue:
            node, idx = queue.popleft()
            if idx == len(word):
                if node.is_word:
                    return True
            else:
                ch = word[idx]
                if ch == '.':
                    for next_ch in node.next:
                        queue.append((node.next[next_ch], idx + 1))
                elif ch in node.next:
                    queue.append((node.next[ch], idx + 1))
        return False
