from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(max_heap)

        prev = ()
        res = []
        while max_heap or prev:
            if prev and not max_heap:
                return ''
            neg_cnt, char = heapq.heappop(max_heap)
            res.append(char)
            neg_cnt += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = ()
            if neg_cnt != 0:
                prev = (neg_cnt, char)

        return ''.join(res)
