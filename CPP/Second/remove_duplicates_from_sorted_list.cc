// https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/

// Given a sorted linked list, delete all duplicates such that each element appear
// For example,
// Given 1->1->2, return 1->2.
// Given 1->1->2->3->3, return 1->2->3.

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
        for (ListNode *p = head; p; p = p->next) {
            auto q = p->next;
            while(q && q->val == p->val) {
                auto tmp = q;
                p->next = q->next;
                q = q->next;
                delete tmp;
            }
        }
        return head;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
