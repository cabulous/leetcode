from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/synonymous-sentences/discuss/430534/Python-bfs-solution
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(dict)
        queue = deque([text])
        res = set()

        for u, v in synonyms:
            graph[u][v] = 1
            graph[v][u] = 1

        while queue:
            curr_text = queue.popleft()
            res.add(curr_text)

            words = curr_text.split()
            for i, word in enumerate(words):
                if word in graph:
                    for new_word in graph[word]:
                        new_text = ' '.join(words[:i] + [new_word] + words[i + 1:])
                        if new_text not in res:
                            queue.append(new_text)

        return sorted(res)
