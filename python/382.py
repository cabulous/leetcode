import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        curr = head
        while curr:
            self.vals.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        pick = int(random.random() * len(self.vals))
        return self.vals[pick]
