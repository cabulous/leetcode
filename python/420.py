# https://leetcode.com/problems/strong-password-checker/discuss/91008/Simple-Python-solution
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 3

        if any('a' <= c <= 'z' for c in password):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1

        change = 0
        one = two = 0
        index = 2

        while index < len(password):
            if password[index] == password[index - 1] == password[index - 2]:
                length = 2
                while index < len(password) and password[index] == password[index - 1]:
                    length += 1
                    index += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                index += 1

        if len(password) < 6:
            return max(missing_type, 6 - len(password))

        if len(password) <= 20:
            return max(missing_type, change)

        delete = len(password) - 20

        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) // 2
        change -= max(delete - one - two * 2, 0) // 3

        return delete + max(missing_type, change)
