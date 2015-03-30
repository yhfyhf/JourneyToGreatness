#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int d = 0;
        for (ListNode *p = headA; p; p = p->next) d++;
        for (ListNode *q = headB; q; q = q->next) d--;
        while (d > 0) {
            headA = headA->next;
            d--;
        }
        while (d < 0) {
            headB = headB->next;
            d++;
        }
        while (headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
