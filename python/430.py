class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        sentinel = Node(0, None, head, None)
        prev = sentinel
        stack = [head]

        while stack:
            curr = stack.pop()
            curr.prev, prev.next = prev, curr
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr

        sentinel.next.prev = None
        return sentinel.next
