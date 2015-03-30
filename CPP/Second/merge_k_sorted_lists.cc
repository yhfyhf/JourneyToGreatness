// https://oj.leetcode.com/problems/merge-k-sorted-lists/

// Merge k sorted linked lists and return it as one sorted list. Analyze and

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};

class Solution {
private:
    struct cmp{
	// C++ 优先队列默认的比较是 x < y 为 true， 输出降序
	// 现在我们要输出升序，只有把默认的 operator (<) 改成 >
	// 这里的 compare 只接受 Object，所以写个 struct
	bool operator()(const ListNode *x, const ListNode *y) {
	    return x->val > y->val;
	}
    };
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
	priority_queue<ListNode*, vector<ListNode *>, cmp> pq;
	for (auto node: lists) {
	    if (node)
		pq.push(node);
	}
	ListNode *head = nullptr, *tail = nullptr;
	while(!pq.empty()) {
	    ListNode *p = pq.top();
	    pq.pop();
	    int x = p->val;
	    if (!head)
		head = tail = new ListNode(x);
	    else {
		tail->next = new ListNode(x);
		tail = tail->next;
	    }
	    p = p->next;
	    if (p)
		pq.push(p);
	}
	return head;
    }
};

int main(int argc, char *argv[])
{
    ListNode *h1 = new ListNode(1);
    h1->next = new ListNode(4);
    h1->next->next = new ListNode(8);
    ListNode *h2 = new ListNode(2);
    h2->next = new ListNode(5);
    ListNode *h3 = new ListNode(6);
    h3->next = new ListNode(7);
    h3->next->next = new ListNode(9);
    vector<ListNode *> v;
    v.push_back(h1);
    v.push_back(h2);
    v.push_back(h3);
    Solution so;
    auto res = so.mergeKLists(v);
    ListNode *p = res;
    while(p) {
	cout<<(p->val)<<" ";
	p = p->next;
    }
    return 0;
}
