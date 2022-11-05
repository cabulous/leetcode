from collections import defaultdict
from typing import List


# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.next[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            node = node.next.get(ch)
            if not node:
                return False
        return node.is_word


class Solution:
    def __init__(self):
        self.board = []
        self.rows = 0
        self.cols = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        for r in range(self.rows):
            for c in range(self.cols):
                self.backtrack(r, c, '', trie.root)

        return self.res

    def backtrack(self, row, col, path, node):
        if node.is_word:
            self.res.append(path)
            node.is_word = False

        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return

        letter = self.board[row][col]
        node = node.next.get(letter)

        if not node:
            return

        self.board[row][col] = '#'

        for dr, dc in self.directions:
            self.backtrack(row + dr, col + dc, path + letter, node)

        self.board[row][col] = letter
