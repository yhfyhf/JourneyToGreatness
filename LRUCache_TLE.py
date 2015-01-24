import collections

class LRUCache:
    # @param capacity, an integer
    # TODO better performance, now 1406 ms
    def __init__(self, capacity):
        self._hmap = dict()
        self._cache = collections.deque()
        self.CAPACITY = capacity
        

    # @return an integer
    def get(self, key):
        if key in self._hmap:
            self._cache.remove((key, self._hmap[key]))
            self._cache.appendleft((key, self._hmap[key]))

            print 'get:', self._hmap, self._cache

            return self._hmap[key]
        else:
            print 'get:', self._hmap, self._cache

            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self._hmap:
            self._cache.appendleft((key, value))
            self._hmap[key] = value
            if len(self._cache) > self.CAPACITY:
                tmp = self._cache.pop()
                self._hmap.pop(tmp[0])
        else:
            self._cache.remove((key, self._hmap[key]))
            self._cache.appendleft((key, value))
            self._hmap[key] = value

        print 'set:', self._hmap, self._cache

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