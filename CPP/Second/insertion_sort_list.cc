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
    ListNode *insertionSortList(ListNode *head) {
        if (!head || !head->next)
            return head;
        ListNode *new_head = new ListNode(-1);
        new_head->next = head;
        ListNode *p = head;
        while (p->next) {
            if (p->next->val < p->val) {
                auto prev = new_head;
                while (prev->next->val <= p->next->val) 
                    prev = prev->next;
                // swap, succ is the one need to swap
                auto succ = p->next;
                p->next = succ->next;
                succ->next = prev->next;
                prev->next= succ;
            }
            else {
                p = p->next;
            }
        }
        return new_head->next;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
