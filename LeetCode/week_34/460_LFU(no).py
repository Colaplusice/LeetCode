class LFUCache:
    def __init__(self, capacity):
        self.dicts = {}
        self.capacity = capacity
        """
        :type capacity: int
        """

    def get(self, key):
        """
               :type key: int
               :rtype: int
                       """
        sd = self.dicts.get(key)
        if sd:
            return sd
        return -1

    def put(self, key, value):
        list_dict = list(self.dicts.items())
        while len(list_dict) >= self.capacity and list_dict:
            list_dict.pop(0)
        self.dicts = dict(list_dict)
        self.dicts[key] = value

        """
        :type key: int
        :type value: int
        :rtype: void
        """


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    cache.get(2)
    cache.get(3)
    cache.put(4, 4)
    cache.get(1)

    pass
# Your LFUCache object will be instantiated and called as such:
# obj.put(key,value)
