#include <iostream>
#include <algorithm>

using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};


ListNode *reverse(ListNode *head) {
    if (!head)
	return nullptr;
    ListNode *prev = head, *succ = head, *now, *tail = head;
    while(succ) {
	now = succ;
	succ = succ->next;
	now->next = prev;
	prev = now;
    }
    tail->next = nullptr;
    return now; // or prev
}

int main(int argc, char *argv[])
{
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    ListNode *p = reverse(head);
    while (p){
	cout<<p->val<<endl;
	p = p->next;
    }
    return 0;
}

