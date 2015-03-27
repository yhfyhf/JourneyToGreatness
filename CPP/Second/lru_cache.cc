// Design and implement a data structure for Least Recently Used (LRU) cache.
// It should support the following operations: get and set.

// get(key) - Get the value (will always be positive) of the key if the key
// exists in the cache, otherwise return -1.
// set(key, value) - Set or insert the value if the key is not already present.
// When the cache reached its capacity, it should invalidate the least recently
// used item before inserting a new item.

#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <unordered_map>
using namespace std;

class LRUCache{
private:
    // list<key, val>, so it.first is key, it.second is val
    typedef list<pair<int, int> > CACHE;
    CACHE cache;
    // unordered_map<key, *<key,val>>
    // cache_map存储 key 及相应key, value的iterator
    unordered_map<int, CACHE::iterator> cache_map;
    int capacity;
    // move accessed key to front
    void touch(int key) {
	pair<int, int> x = *cache_map[key];
	cache.erase(cache_map[key]);
	cache.push_front(x);
	cache_map[x.first] = cache.begin();
    }
    
public:
    LRUCache(int capacity) {
	this->capacity = capacity;
    }

    
    int get(int key) {
	if (cache_map.find(key) == cache_map.end())
	    return -1;
	touch(key);
	return cache.begin()->second;
    }

    void set(int key, int value) {
	if (cache_map.find(key) != cache_map.end()) {
	    touch(key);
	    cache.begin()->second = value;
	} else {
	    if (cache.size() >= capacity) {	
		cache_map.erase(cache.rbegin()->first);
		cache.pop_back();
	    }
	    cache.push_front(make_pair(key, value));
	    cache_map[key] = cache.begin();
	}
    }
};

int main(int argc, char *argv[])
{
    LRUCache lru(3);
    lru.set(1,10);
    lru.set(2, 20);
    lru.set(3, 30);
    cout<<lru.get(2)<<endl;
    cout<<lru.get(4)<<endl;
    return 0;
}
