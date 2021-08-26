class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2

        return slots == 0


# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78560/Simple-Python-solution-using-stack.-With-Explanation./83341
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder, stack = preorder.split(','), []
        for node in preorder:
            while stack and node == stack[-1] == '#':
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(node)
        return stack == ['#']
