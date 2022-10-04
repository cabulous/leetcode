from collections import deque


class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if root is None:
            return False

        sum -= root.val

        if root.left is None and root.right is None:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if root is None:
            return False

        queue = deque([(root, sum - root.val)])

        while queue:
            node, remaining = queue.popleft()
            if node.left is None and node.right is None and remaining == 0:
                return True

            if node.left:
                queue.append((node.left, remaining - node.left.val))
            if node.right:
                queue.append((node.right, remaining - node.right.val))

        return False
