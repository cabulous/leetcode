class Solution:
    def pseudoPalindromicPaths(self, root) -> int:
        count = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node:
                path ^= (1 << node.val)
                if not node.left and not node.right:
                    count += 1 if path & (path - 1) == 0 else 0
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))
        return count
