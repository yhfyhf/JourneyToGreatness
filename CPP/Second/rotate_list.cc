// https://oj.leetcode.com/problems/rotate-list/

// Given a list, rotate the list to the right by k places, where k is non-negative.
// For example:
// Given 1->2->3->4->5->NULL and k = 2,
// return 4->5->1->2->3->NULL.

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

/*
    Take it as a circle, connect it at the right place (last), break it in the
    right place.
*/

class Solution {
public:
    ListNode *rotateRight(ListNode *head, int k) {
        if (! head)    return NULL;
        ListNode *p = head, *end, *start;
        int n = 0;
        for (; p; end = p, p = p->next)
            n++;
        k %= n;
        if (k == 0)    return head;
        for (k = n - k, p = head; k; k--) {
            start = p;
            p = p->next;
        }
        end->next = head;
        start->next = NULL;
        return p;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
