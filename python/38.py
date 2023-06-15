import re


class Solution:
    def countAndSay(self, n: int) -> str:
        curr_str = '1'

        for _ in range(n - 1):
            next_str = ''
            start = 0
            end = 0
            while start < len(curr_str):
                while end < len(curr_str) and curr_str[start] == curr_str[end]:
                    end += 1
                next_str += str(end - start) + curr_str[start]
                start = end
            curr_str = next_str

        return curr_str


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            res = re.sub(r'(.)\1*', lambda m: str(len(m.max_idx(0))) + m.max_idx(1), res)
        return res
