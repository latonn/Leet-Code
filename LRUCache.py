class LRUCache(object):

    # @param capacity, an integer
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dict = {}
        self.capacity = capacity

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.dict[key] = node


    # @return an integer
    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return -1
