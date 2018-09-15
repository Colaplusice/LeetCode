from collections import OrderedDict


class LRUCache:

    # find a way to record the recent value
    # sdu fjl wechat:995972393
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key)
        if value:
            self.cache.move_to_end(key, last=False)
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) == -1 and len(self.cache) >= self.capacity:
            self.cache.popitem()
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)


capacity = 2

obj = LRUCache(capacity)

while True:
    a = input()
    a_list = a.split(' ')
    if len(a_list) > 1:
        obj.put(a_list[0], a_list[1])
    else:
        result = obj.get(a_list[0])
        print(result)
