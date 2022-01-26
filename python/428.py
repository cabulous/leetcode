from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions
class Codec:
    def serialize(self, root: 'Node') -> str:
        vals = []

        def helper(node):
            if node is None:
                return
            vals.append(str(node.val))
            for kid in node.children:
                helper(kid)
            vals.append('#')

        helper(root)
        return ' '.join(vals)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None

        vals = deque(data.split())
        root = Node(int(vals.popleft()), [])

        def helper(node):
            if node is None:
                return

            while vals[0] != '#':
                val = vals.popleft()
                kid = Node(int(val), [])
                node.children.append(kid)
                helper(kid)

            vals.popleft()

        helper(root)
        return root
