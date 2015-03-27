// https://oj.leetcode.com/problems/add-two-numbers/

// You are given two linked lists representing two non-negative numbers. The
// digits are stored in reverse order and each of their nodes contain a single
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8

/**
 * Definition for singly-linked list.
 */
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        // initialize new structs
        ListNode dummy(0);
        ListNode *p = &dummy;
        int carry = 0;
        while (l1 || l2) {
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            // use new when assign memory to pointer
            p->next = new ListNode(carry%10);
            p = p->next;
            carry /= 10;
        }
        if (carry)
            p->next = new ListNode(carry);
        // return type is pointer, dummy->next is struct, dummy.next is pointer
        return dummy.next;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
