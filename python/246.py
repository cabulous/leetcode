# hashmap
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        rotated = []
        for n in reversed(num):
            if n not in rotated_digits:
                return False
            rotated.append(rotated_digits[n])
        return ''.join(rotated) == num


# two pointers
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in rotated_digits:
                return False
            if rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
