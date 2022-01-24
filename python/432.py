# https://leetcode.com/problems/all-oone-data-structure/discuss/91401/Python-O(1)-doubly-linked-list-and-dictionary
class Block:

    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None

    def append(self, new_block):
        new_block.prev, new_block.next = self, self.next
        self.next.prev, self.next = new_block, new_block


class AllOne:

    def __init__(self):
        self.begin = Block()
        self.end = Block()
        self.begin.next = self.end
        self.end.prev = self.begin
        self.mapping = {}

    def inc(self, key: str) -> None:
        if key not in self.mapping:
            curr_block = self.begin
        else:
            curr_block = self.mapping[key]
            curr_block.keys.remove(key)

        if curr_block.val + 1 == curr_block.next.val:
            new_block = curr_block.next
        else:
            new_block = Block(curr_block.val + 1)
            curr_block.append(new_block)

        new_block.keys.add(key)
        self.mapping[key] = new_block

        if not curr_block.keys and curr_block.val != 0:
            curr_block.remove()

    def dec(self, key: str) -> None:
        if key not in self.mapping:
            return

        curr_block = self.mapping[key]
        del self.mapping[key]
        curr_block.keys.remove(key)

        if curr_block.val != 1:
            if curr_block.val - 1 == curr_block.prev.val:
                new_block = curr_block.prev
            else:
                new_block = Block(curr_block.val - 1)
                curr_block.prev.append(new_block)
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not curr_block.keys:
            curr_block.remove()

    def getMaxKey(self) -> str:
        if self.end.prev.val == 0:
            return ''
        key = self.end.prev.keys.pop()
        self.end.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.begin.next.val == 0:
            return ''
        key = self.begin.next.keys.pop()
        self.begin.next.keys.add(key)
        return key
