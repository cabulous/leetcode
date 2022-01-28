from collections import defaultdict, deque


# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/59725/Python-easy-to-follow-solution-using-Trie./507243
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        stack = deque([(self.root, 0)])
        while stack:
            node, index = stack.popleft()
            if index == len(word):
                if node.is_word:
                    return True
            elif word[index] == '.':
                for kid in node.children:
                    stack.append((node.children[kid], index + 1))
            elif word[index] in node.children:
                stack.append((node.children[word[index]], index + 1))
        return False
