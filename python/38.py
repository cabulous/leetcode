import re


class Solution:
    def countAndSay(self, n: int) -> str:
        curr_string = '1'

        for _ in range(n - 1):
            next_string = ''
            start = 0
            end = 0
            while start < len(curr_string):
                while end < len(curr_string) and curr_string[end] == curr_string[start]:
                    end += 1
                next_string += str(end - start) + curr_string[start]
                start = end
            curr_string = next_string

        return curr_string


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            res = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), res)
        return res
