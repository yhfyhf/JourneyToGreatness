// https://oj.leetcode.com/problems/reverse-linked-list-ii/

// Reverse a linked list from position m to n. Do it in-place and in one-pass.
// For example:
// Given 1->2->3->4->5->NULL, m = 2 and n = 4,
// return 1->4->3->2->5->NULL.
// Note:
// Given m, n satisfy the following condition:
// 1 ≤ m ≤ n ≤ length of list.

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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode *p = &dummy;
		// move m-1 steps
        for (int i = 0; i < m - 1; i++)
            p = p->next;
        
        ListNode *succ = p->next;
		// do n-m-1 times switch
        for (int i = m; i < n ; i++) {
            ListNode *tmp = p->next;
            p->next = succ->next;
            succ->next = succ->next->next;
            p->next->next = tmp;
        }
        return dummy.next;
        
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
