// https://oj.leetcode.com/problems/partition-list/

// Given a linked list and a value x, partition it such that all nodes less than x
// You should preserve the original relative order of the nodes in each of the two
// For example,
// Given 1->4->3->2->5->2 and x = 3,
// return 1->2->2->4->3->5.

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
    ListNode *partition(ListNode *head, int x) {
        ListNode dummy1(-1);
        ListNode dummy2(-1);
        ListNode *p = &dummy1, *q = &dummy2;
        for (ListNode *t = head; t; t = t->next) {
            if (t->val < x) {
                p->next = new ListNode(t->val);
                p = p->next;
            }
            else {
                q->next = new ListNode(t->val);
                q = q->next;
            }
        }
        p->next = dummy2.next;
        q->next = nullptr;
        return dummy1.next;
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
