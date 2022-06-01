class NestedInteger:
    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> [NestedInteger]:
        pass


# https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C%2B%2B
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        self.hasNext()
        nested_list, index = self.stack[-1]
        self.stack[-1][1] += 1
        return nested_list[index].getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            nested_list, index = self.stack[-1]
            if index == len(nested_list):
                self.stack.pop()
            else:
                item = nested_list[index]
                if item.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([item.getList(), 0])
        return False
