from typing import List
from collections import defaultdict


# https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer/322524
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        word_set = set(wordList)
        layer = {beginWord: [[beginWord]]}

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
            word_set -= set(new_layer.keys())
            layer = new_layer

        return []
