class Solution:
    def compress(self, chars: list[str]) -> int:
        read_idx = 0
        write_idx = 0

        while read_idx < len(chars):
            ch = chars[read_idx]
            count = 0

            while read_idx < len(chars) and chars[read_idx] == ch:
                count += 1
                read_idx += 1

            chars[write_idx] = ch
            write_idx += 1

            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1

        return write_idx
