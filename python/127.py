from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        word_len = len(beginWord)
        all_combo_dict = defaultdict(list)

        for w in wordList:
            for i in range(word_len):
                all_combo_dict[w[:i] + '*' + w[i + 1:]].append(w)

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, level = queue.popleft()
            for i in range(word_len):
                intermediate_word = word[:i] + '*' + word[i + 1:]
                for w in all_combo_dict[intermediate_word]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited.add(w)
                        queue.append((w, level + 1))
                all_combo_dict[intermediate_word] = []

        return 0


class Solution:
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def visit_word_node(self, queue, visited, others_visited):
        cur_word, level = queue.popleft()
        for i in range(self.length):
            intermediate_word = cur_word[:i] + '*' + cur_word[i + 1:]
            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_begin and queue_end:
            ans = self.visit_word_node(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visit_word_node(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
