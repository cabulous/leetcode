class Solution:
    def average(self, salary: list[int]) -> float:
        middle = sorted(salary)[1:-1]
        return sum(middle) / len(middle)
