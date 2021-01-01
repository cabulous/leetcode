# recursion
class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# iteration
class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root:
            return False
        queue = [(root, sum - root.val), ]
        while queue:
            node, cur_sum = queue.pop()
            if not node.left and not node.right and cur_sum == 0:
                return True
            if node.left:
                queue.append((node.left, cur_sum - node.left.val))
            if node.right:
                queue.append((node.right, cur_sum - node.right.val))
        return False
