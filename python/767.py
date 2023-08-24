from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(max_heap)

        prev = ()
        res = []
        while max_heap or prev:
            if prev and not max_heap:
                return ''
            neg_count, char = heapq.heappop(max_heap)
            res.append(char)
            neg_count += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = ()
            if neg_count != 0:
                prev = (neg_count, char)

        return ''.join(res)
