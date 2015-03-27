// https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

// Given a linked list, remove the nth node from the end of list and return its
// For example,
//    Given linked list: 1->2->3->4->5, and n = 2.
//    After removing the second node from the end, the linked list becomes
// Note:
// Given n will always be valid.
// Try to do this in one pass.

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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode **p = &head, *q = head;
        while (n--)
            q = q->next;
        while (q) {
            p = &(*p)->next;
            q = q->next;
        }
        // *p is the one need to be deleted
        q = (*p)->next;
        delete *p;
        *p = q;
        return head;

    }
};

int main(int argc, char *argv[])
{

    return 0;
}
