class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._next = iterator.next()

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        res = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return res

    def hasNext(self):
        return self._next is not None
