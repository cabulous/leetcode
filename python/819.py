import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(w for w in words if w not in ban)
        return count.most_common()[0][0]
