class Solution:
    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        word_end_key = '#'
        max_row, max_col = len(board), len(board[0])
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        trie = {}
        matched_words = []

        for word in words:
            node = trie
            for w in word:
                node = node.setdefault(w, {})
            node[word_end_key] = word

        def backtrack(row, col, parent):
            # terminator
            letter = board[row][col]
            cur_node = parent[letter]
            match = cur_node.pop(word_end_key, False)

            if match:
                matched_words.append(match)

            # recursion
            board[row][col] = '#'
            for k in range(4):
                nr, nc = row + dx[k], col + dy[k]
                if 0 <= nr < max_row and 0 <= nc < max_col and board[nr][nc] in cur_node:
                    backtrack(nr, nc, cur_node)

            # recover states
            board[row][col] = letter

            # optimization
            if not cur_node:
                parent.pop(letter)

        for i in range(max_row):
            for j in range(max_col):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return matched_words
