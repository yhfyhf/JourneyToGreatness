// https://oj.leetcode.com/problems/swap-nodes-in-pairs/

// Given a linked list, swap every two adjacent nodes and return its head.
// For example,
// Given 1->2->3->4, you should return the list as 2->1->4->3.
// Your algorithm should use only constant space. You may not modify the values in

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
    ListNode *swapPairs(ListNode *head) {
        ListNode **p = &head;
        while ((*p) && (*p)->next) {
            ListNode *tmp = (*p);
            (*p) = (*p)->next;
            tmp->next = (*p)->next;
            (*p)->next = tmp;

            p = &(*p)->next->next;
        }
        return head;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
