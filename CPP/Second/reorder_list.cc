#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

void print_list(ListNode *head) {
    auto *p = head;
    while(p){
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;
}


class Solution {
public:
    void reorderList(ListNode *head) {
        if (! head || !head->next)
            return ;
        ListNode *p = head, *new_head = head, *prev;
        // find mid pointer and cut
        while (p && p->next) {
            prev = new_head;
            new_head = new_head->next;
            p = p->next->next;
        }
        prev->next = nullptr;
        // reverse the second half
        new_head = reverse(new_head);
        print_list(head);
        print_list(new_head);
        // merget two linked list
        p = head;
        ListNode *tmp;
        // p might be the shorter one
        while(p->next) {
            tmp = new_head;
            new_head = new_head->next;
            tmp->next = p->next;
            p->next = tmp;
            p = tmp->next;
        }
        p->next = new_head;

    }

    ListNode* reverse(ListNode *head) {
        if (!head)
            return nullptr;
        ListNode *p = head, *curr = head, *tmp, *tail = head;
        while(curr) {
            tmp = curr;
            curr = curr->next;
            tmp->next = p;
            p = tmp;
        }
        tail->next = nullptr;
        return p;
    }
};

int main(int argc, char *argv[])
{
    ListNode *head = new ListNode(1);
    // head->next = new ListNode(2);
    // head->next->next = new ListNode(3);
    // head->next->next->next = new ListNode(4);
    // head->next->next->next->next = new ListNode(5);
    // head->next->next->next->next->next = new ListNode(6);

    Solution s;
    s.reorderList(head);
    print_list(head);
    return 0;
}
