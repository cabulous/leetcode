from typing import Generator


class NestedInteger:
    pass


# Using a Generator
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self.int_generator(nestedList)
        self.peeked = None

    def int_generator(self, nested_list) -> "Generator[int]":
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self.int_generator(nested.getList())

    def next(self) -> int:
        if not self.hasNext():
            return -1
        next_integer, self.peeked = self.peeked, None
        return next_integer

    def hasNext(self) -> bool:
        if self.peeked is not None:
            return True
        try:
            self.peeked = next(self.generator)
            return True
        except:
            return False


# https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C%2B%2B
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        self.hasNext()
        nested_list, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nested_list[i].getInteger()

    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nested_list, i = s[-1]
            if i == len(nested_list):
                s.pop()
            else:
                x = nested_list[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


# Two Stacks
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def make_stack_top_an_integer(self):
        while self.stack:
            curr_list, curr_index = self.stack[-1]
            if len(curr_list) == curr_index:
                self.stack.pop()
                continue
            if curr_list[curr_index].isInteger():
                break
            new_list = curr_list[curr_index].getList()
            self.stack[-1][1] += 1
            self.stack.append([new_list, 0])

    def next(self) -> int:
        self.make_stack_top_an_integer()
        curr_list, curr_index = self.stack[-1]
        self.stack[-1][1] += 1
        return curr_list[curr_index].getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0


# Stack
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0

    def make_stack_top_an_integer(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))


# Make a Flat List with Recursion
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.integers = []
        self.position = -1

        def flatten_list(nested_list):
            for nested_int in nested_list:
                if nested_int.isInteger():
                    self.integers.append(nested_int)
                else:
                    flatten_list(nested_int.getList())

        flatten_list(nestedList)

    def next(self) -> int:
        self.position += 1
        return self.integers[self.position]

    def hasNext(self) -> bool:
        return self.position + 1 < len(self.integers)
