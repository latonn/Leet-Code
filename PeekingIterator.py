# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peekFlag = False
        self.nextElement = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:
            self.nextElement = self.iter.next()
            self.peekFlag = True
        return self.nextElement

    def next(self):
        """
        :rtype: int
        """
        if not self.peekFlag:
            return self.iter.next()
        nextElement = self.nextElement
        self.peekFlag = False
        self.nextElement = None
        return nextElement

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekFlag or self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
