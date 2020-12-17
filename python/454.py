class Solution:
    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        count = 0
        m = {}
        for a in A:
            for b in B:
                m[a + b] = m.get(a + b, 0) + 1
        for c in C:
            for d in D:
                count += m.get(-c - d, 0)
        return count


class Solution:
    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        m = {}

        def n_sum_count(lists):
            add_to_hash(lists, 0, 0)
            return count_complements(lists, len(lists) // 2, 0)

        def add_to_hash(lists, i, sum):
            if i == len(lists) // 2:
                m[sum] = m.get(sum, 0) + 1
            else:
                for num in lists[i]:
                    add_to_hash(lists, i + 1, sum + num)

        def count_complements(lists, i, complement):
            if i == len(lists):
                return m.get(complement, 0)
            count = 0
            for num in lists[i]:
                count += count_complements(lists, i + 1, complement - num)
            return count

        return n_sum_count([A, B, C, D])
