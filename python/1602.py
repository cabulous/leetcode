from collections import deque


# two deque
class Solution:
    def findNearestRightNode(self, root, u):
        if not root:
            return None

        next_level = deque([root])
        while next_level:
            curr_level = next_level
            next_level = deque()
            while curr_level:
                node = curr_level.popleft()
                if node == u:
                    return curr_level.popleft() if curr_level else None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return None


# one deque
class Solution:
    def findNearestRightNode(self, root, u):
        if not root:
            return None

        queue = deque([root, None, ])

        while queue:
            node = queue.popleft()
            if node == u:
                return queue.popleft()
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
