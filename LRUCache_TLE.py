import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.CAPACITY = capacity
        self._cache = collections.deque()
        self._map = dict()

    # @return an integer
    def get(self, key):
        if key in self._map:
            v = self._map[key]
            self._cache.remove((key, v))
            self._cache.appendleft((key, v))
            return v
        else:
            return -1
            
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self._map:
            self._cache.remove((key, self._map[key]))
            self._cache.appendleft((key, value))
            self._map[key] = value
        else:
            self._cache.appendleft((key, value))
            self._map[key] = value
            if len(self._cache) > self.CAPACITY:
                kv = self._cache.pop()
                self._map.pop(kv[0])
if __name__ == '__main__':
    lru = LRUCache(1)
    #Testcase 1
    # lru.set(2,1)
    # lru.get(2)
    # lru.set(3,2)
    # lru.get(2)
    # lru.get(3)

    lru.get(0)
    # lru.set(2,1)
    # lru.set(2,2)
    # lru.get(2)
    # lru.set(1,1)
    # lru.set(4,1)
    # lru.get(2)
