class Solution:
    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        word_end_key = '#'
        trie = {}
        m, n = len(board), len(board[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        output = []

        for word in words:
            node = trie
            for w in word:
                node = node.setdefault(w, {})
            node[word_end_key] = word

        def backtrack(row, col, parent):
            letter = board[row][col]
            cur_node = parent[letter]
            match = cur_node.pop(word_end_key, False)

            if match:
                output.append(match)

            board[row][col] = '#'
            for neighbor in neighbors:
                nr, nc = row + neighbor[0], col + neighbor[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in cur_node:
                    backtrack(nr, nc, cur_node)

            board[row][col] = letter

            if not cur_node:
                parent.pop(letter)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return output
