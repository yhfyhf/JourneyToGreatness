#include <iostream>
#include <algorithm>
#include <list>
#include <unordered_map>
#include <cassert>
#include <stack>
using namespace std;

class LRUCache{
private:
    // linkedlist of <key, val>
    typedef list<pair<int, int> > CACHE;
    CACHE cache;
    // unordered_map<key, *<key, val> >
    unordered_map<int, CACHE::iterator> hash;
    int capacity;
    // move accesed key to front
    void touch(int key) {
	// * to get the value
	pair<int, int> x = *hash[key];
	cache.erase(hash[key]);
	cache.push_front(x);
	hash[x.first] = cache.begin();
    }

public:
    LRUCache(int capacity) {
	this->capacity = capacity;
    }

    int get(int key) {
	if (hash.find(key) == hash.end())
	    return -1;
	else {
	    touch(key);
	    return cache.begin()->second;
	}
    }
    void set(int key, int value) {
	if (hash.find(key) != hash.end()) {
	    touch(key);
	    cache.begin()->second = value;
	} else {
	    if (cache.size() >= capacity) {
		hash.erase(cache.rbegin()->first);
		cache.pop_back();
	    }
	    cache.push_front(make_pair(key, value));
	    hash[key] = cache.begin();
	}
    }
};

void test(){
    LRUCache lru(3);
    lru.set(1, 10);
    lru.set(2, 20);
    lru.set(3, 30);
    assert(lru.get(2)==20);
    cout<<(lru.get(2)==20)<<endl;
    cout<<(lru.get(4)==-1)<<endl;
}


// The main function to find the maximum rectangular area under given
// histogram with n bars
int getMaxArea(int hist[], int n)
{
    // Create an empty stack. The stack holds indexes of hist[] array
    // The bars stored in stack are always in increasing order of their
    // heights.
    stack<int> s;
 
    int max_area = 0; // Initalize max area
    int tp;  // To store top of stack
    int area_with_top; // To store area with top bar as the smallest bar
 
    // Run through all bars of given histogram
    int i = 0;
    while (i < n)
    {
        // If this bar is higher than the bar on top stack, push it to stack
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);
 
        // If this bar is lower than top of stack, then calculate area of rectangle 
        // with stack top as the smallest (or minimum height) bar. 'i' is 
        // 'right index' for the top and element before top in stack is 'left index'
        else
        {
            tp = s.top();  // store the top index
            s.pop();  // pop the top
 
            // Calculate the area with hist[tp] stack as smallest bar
            area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
	    cout<<"hist[tp]:"<<hist[tp]<<"\twidth:"<<(s.empty() ? i : i - s.top() - 1)<<endl;
	    cout<<"area_with_top:"<<area_with_top<<endl;
            // update max area, if needed
            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }
 
    // Now pop the remaining bars from stack and calculate area with every
    // popped bar as the smallest bar
    while (s.empty() == false)
    {
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
 
        if (max_area < area_with_top)
            max_area = area_with_top;
    }
 
    return max_area;
}


int main(int argc, char *argv[])
{
    int hist[] = {6, 2, 5, 4, 5, 1, 6};
    int n = sizeof(hist)/sizeof(hist[0]);
    cout << "Maximum area is " << getMaxArea(hist, n);
    return 0;
}
