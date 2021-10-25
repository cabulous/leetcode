from collections import defaultdict


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
        for w in word:
            node = node.next[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.next.get(w)
            if not node:
                return False
        return node.is_word


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.board = []
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.res = []

    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        self.rows, self.cols = len(board), len(board[0])
        self.board = board

        trie = Trie()
        for word in words:
            trie.insert(word)

        for row in range(self.rows):
            for col in range(self.cols):
                self.backtrack(row, col, '', trie.root)

        return self.res

    def backtrack(self, row, col, path, node):
        if node.is_word:
            self.res.append(path)
            node.is_word = False

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        letter = self.board[row][col]
        node = node.next.get(letter)

        if not node:
            return

        self.board[row][col] = '#'

        for dr, dc in self.directions:
            self.backtrack(row + dr, col + dc, path + letter, node)

        self.board[row][col] = letter
