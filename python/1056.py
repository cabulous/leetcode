class Solution:
    def confusingNumber(self, n: int) -> bool:
        lookup = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        rotated_number = []

        for ch in str(n):
            if ch not in lookup:
                return False
            rotated_number.append(lookup[ch])

        return int(''.join(rotated_number)[::-1]) != n
