# top down
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True

        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        return abs(height(root.left) - height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


# bottom up
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True

        def helper(node):
            if not node:
                return True, -1
            left_is_balanced, left_height = helper(node.left)
            if not left_is_balanced:
                return False, 0
            right_is_balanced, right_height = helper(node.right)
            if not right_is_balanced:
                return False, 0
            return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

        return helper(root)[0]
