from collections import defaultdict


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') == 0


class Solution:
    def checkRecord(self, s: str) -> bool:
        index = defaultdict(set)
        for i, ch in enumerate(s):
            index[ch].add(i)

        if len(index['A']) >= 2:
            return False

        if len(index['L']) < 3:
            return True

        idx_set = index['L']
        consecutive = 1

        for num in idx_set:
            if num - 1 not in idx_set:
                curr = 1
                next_num = num + 1
                while next_num in idx_set:
                    curr += 1
                    next_num += 1
                consecutive = max(consecutive, curr)

        return consecutive < 3
