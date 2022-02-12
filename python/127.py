from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                intermediate_word = word[:i] + '*' + word[i + 1:]
                for next_word in all_combo_dict[intermediate_word]:
                    if next_word == endWord:
                        return level + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                all_combo_dict[intermediate_word].clear()

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        curr = deque([beginWord])
        other = deque([endWord])
        visited = {beginWord, endWord}
        step = 1

        while curr:
            if len(curr) > len(other):
                curr, other = other, curr

            nxt = deque()

            while curr:
                word = curr.popleft()
                for i in range(len(word)):
                    intermediate_word = word[:i] + '*' + word[i + 1:]
                    for next_word in all_combo_dict[intermediate_word]:
                        if next_word in other:
                            return step + 1
                        if next_word not in visited:
                            visited.add(next_word)
                            nxt.append(next_word)
                    all_combo_dict[intermediate_word].clear()

            step += 1
            curr = nxt

        return 0
