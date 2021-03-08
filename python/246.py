# hashmap
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        rotated = []
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated.append(rotated_digits[c])
        rotated_str = ''.join(rotated)
        return rotated_str == num


# two pointers
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in rotated_digits or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


# make rotate copy
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = []
        for c in reversed(num):
            if c in {'0', '1', '8'}:
                rotated.append(c)
            elif c == '6':
                rotated.append('9')
            elif c == '9':
                rotated.append('6')
            else:
                return False
        rotated_str = ''.join(rotated)
        return rotated_str == num
