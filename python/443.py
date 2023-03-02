class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1

            chars[res] = ch
            res += 1

            if count > 1:
                for c in str(count):
                    chars[res] = c
                    res += 1

        return res
