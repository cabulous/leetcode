from collections import defaultdict
from typing import List


# https://leetcode.com/problems/design-in-memory-file-system/discuss/426854/python-scalable-trie-solution

class Node:

    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ''


class FileSystem:

    def __init__(self):
        self.root = Node()

    def find(self, path: str, create=False):
        node = self.root
        if len(path) == 1:
            return node
        for word in path.split('/')[1:]:
            if not node.child.get(word) and not create:
                return None
            node = node.child[word]
        return node

    def ls(self, path: str) -> List[str]:
        node = self.find(path)
        if node.content:
            return [path.split('/')[-1]]
        return sorted(node.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.find(filePath, True)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.find(filePath)
        return node.content
