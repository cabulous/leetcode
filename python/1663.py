class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z_count, remainder = divmod(k - n - 1, 25)
        a_count = n - z_count - 1
        return 'a' * a_count + chr(ord('a') + remainder + 1) + 'z' * z_count

