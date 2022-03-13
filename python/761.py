class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start_index = 0
        res = []

        for end_index, val in enumerate(s):
            count += 1 if val == '1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[start_index + 1:end_index]) + '0')
                start_index = end_index + 1

        return ''.join(sorted(res, reverse=True))
