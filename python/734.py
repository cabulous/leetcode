from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        lookup = defaultdict(set)
        for word1, word2 in similarPairs:
            lookup[word1].add(word2)
            lookup[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence2[i] in lookup[sentence1[i]]:
                continue
            return False

        return True
