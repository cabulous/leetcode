from collections import defaultdict


class TrieNode:

    def __init__(self, name=''):
        self.node = defaultdict(TrieNode)
        self.name = name
        self.val = -1


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        components = path.split('/')
        curr = self.root

        for i in range(1, len(components)):
            name = components[i]
            if name not in curr.node:
                if i == len(components) - 1:
                    curr.node[name] = TrieNode(name)
                else:
                    return False
            curr = curr.node[name]

        if curr.val != -1:
            return False

        curr.val = value

        return True

    def get(self, path: str) -> int:
        curr = self.root
        components = path.split('/')
        for name in components[1:]:
            if name not in curr.node:
                return -1
            curr = curr.node[name]
        return curr.val
