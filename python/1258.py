from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/synonymous-sentences/discuss/430534/Python-bfs-solution
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(set)
        for u, v in synonyms:
            graph[u].add(v)
            graph[v].add(u)

        queue = deque([text])
        res = set()

        while queue:
            curr_text = queue.popleft()
            res.add(curr_text)

            words = curr_text.split()
            for i, word in enumerate(words):
                for next_word in graph[word]:
                    next_text = ' '.join(words[:i] + [next_word] + words[i + 1:])
                    if next_text not in res:
                        queue.append(next_text)

        return sorted(res)
