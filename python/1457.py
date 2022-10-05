from collections import deque


# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/648534/JavaC%2B%2BPython-At-most-one-odd-occurrence
class Solution:
    def pseudoPalindromicPaths(self, root) -> int:
        return self.helper(root)

    def helper(self, node, count=0):
        if node is None:
            return 0

        count ^= 1 << (node.val - 1)
        res = self.helper(node.left, count) + self.helper(node.right, count)

        if node.left is None and node.right is None:
            if count & (count - 1) == 0:
                res += 1

        return res


class Solution:
    def pseudoPalindromicPaths(self, root) -> int:
        res = 0
        queue = deque([(root, 0)])

        while queue:
            node, count = queue.popleft()
            count ^= 1 << (node.val - 1)

            if node.left is None and node.right is None:
                if count & (count - 1) == 0:
                    res += 1

            if node.left:
                queue.append((node.left, count))
            if node.right:
                queue.append((node.right, count))

        return res
