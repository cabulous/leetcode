from collections import defaultdict


class TrieNode:

    def __init__(self, name='', val=-1):
        self.next = defaultdict(TrieNode)
        self.name = name
        self.val = val


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        components = path.split('/')

        for i in range(1, len(components)):
            name = components[i]
            if name not in curr.next:
                if i == len(components) - 1:
                    curr.next[name] = TrieNode(name, value)
                    return True
                return False
            curr = curr.next[name]

        if curr.val != -1:
            return False

        curr.val = value

        return True

    def get(self, path: str) -> int:
        curr = self.root
        components = path.split('/')

        for name in components[1:]:
            if name not in curr.next:
                return -1
            curr = curr.next[name]

        return curr.val
