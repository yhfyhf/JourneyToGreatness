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
    ListNode *sortList(ListNode *head) {
        // zero or one element
        if (head == nullptr || head->next == nullptr)
            return head;
        ListNode *fast = head, *slow = head;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        fast = slow;
        slow = slow->next;
        fast->next = nullptr;
        auto head1 = sortList(head);
        auto head2 = sortList(slow);
        return merge(head1, head2);
    }
    
    ListNode *merge(ListNode *head1, ListNode *head2) {
        ListNode *new_head = new ListNode(-1);
        ListNode *p = new_head;
        while (head1 && head2) {
            if (head1->val < head2->val) {
                p->next = head1;
                head1 = head1->next;
            }
            else {
                p->next = head2;
                head2 = head2->next;
            }
            p = p->next;
        }
        if (head1)
            p->next = head1;
        else
            p->next = head2;
        return new_head->next;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
