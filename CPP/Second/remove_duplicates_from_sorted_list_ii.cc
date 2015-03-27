// https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

// Given a sorted linked list, delete all nodes that have duplicate numbers,
// For example,
// Given 1->2->3->3->4->4->5, return 1->2->5.
// Given 1->1->1->2->3, return 2->3.

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
using namespace std;

class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode **p = &head, *fast, *tmp;
        while(*p) {
            fast = (*p)->next;
	    // delete following same node
            if(fast && (*p)->val == fast->val) {
                do {
                    tmp = fast->next;
                    delete fast;
                    fast = tmp;
                } while(fast && (*p)->val == fast->val);
		// delete current node
                delete *p;
                *p = fast;
            }
            else {
                p = &(*p)->next;
            }
        }
        return head;

    }
};

int main(int argc, char *argv[])
{

    return 0;
}
