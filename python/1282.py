from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        count = defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [people[i:i + size] for size, people in count.items() for i in range(0, len(people), size)]
