# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        vals = []

        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('#')

        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        vals = iter(data.split())

        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        return helper()
