from typing import List
from collections import defaultdict


# https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104122/Python-Straightforward-with-Explanation
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_by_content = defaultdict(list)

        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, content = file.split('(')
                paths_by_content[content[:-1]].append(f'{root}/{name}')

        return [p for p in paths_by_content.values() if len(p) > 1]
