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
        s = self.stack
        while s:
            nested_list, index = s[-1]
            if index == len(nested_list):
                s.pop()
            else:
                x = nested_list[index]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
