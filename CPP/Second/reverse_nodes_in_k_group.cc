// https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

// Given a linked list, reverse the nodes of a linked list k at a time and return
// If the number of nodes is not a multiple of k then left-out nodes in the end
// You may not alter the values in the nodes, only nodes itself may be changed.
// Only constant memory is allowed.
// For example,
// Given this linked list: 1->2->3->4->5
// For k = 2, you should return: 2->1->4->3->5
// For k = 3, you should return: 3->2->1->4->5

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
#include <thread>
#include <chrono>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

void print_list(ListNode *head) {
    while(head) {
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}

// class Solution {
// public:
//     ListNode *reverseKGroup(ListNode *head, int k) {
//         ListNode **p = &head;
//         while (1) {
//             // return value, this is important
//             (*p) = reverse((*p), k);
//             for (int i = 0; i < k; i++){
//                 if(!(*p))
//                     return head;
//                 p = &(*p)->next;
//             }
//         }
//     }

//     ListNode *reverse(ListNode *head, int k) {
//         /*
//             reverse from head to kth node
//             return the first node
//         */
//         ListNode **p = &head, *curr = head;
//         // test whether its length is smaller than k
//         for (int i = 0; i < k; i++) {
//             if (!curr)
//                 return head;
//             curr = curr->next;
//         }
//         curr = head;
//         ListNode *tmp, *end = head;
//         for (int i = 0; i < k; i++) {
//             tmp = curr;
//             curr = curr->next;
//             tmp->next = (*p);
//             (*p) = tmp;
//         }
//         end->next = curr;
//         return (*p);
//     }

// };

class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        ListNode *p = head, *start = head;
        while (1) {
            // count k nodes, if not, finsihed
            for (int i =  0; i < k; i++) {
                if (p)
                    p = p->next;
                else
                    return head;
            }
            reverse(start, k);
            start = p;
        }
        // useless, only to pleasure the compiler
        return head;
    }
    void reverse(ListNode *head, int k) {
        ListNode *succ = head, *end = head, *now = head, *prev = head;
        for (int i = 0; i < k; i++) {
            now = succ;
            succ = succ->next;
            now->next = prev;
            prev = now;
        }
        end->next = succ;
    }
};

int main(int argc, char *argv[])
{
    // 1->2->3->4->5
    ListNode *p = new ListNode(1);
    p->next = new ListNode(2);
    p->next->next = new ListNode(3);
    p->next->next->next = new ListNode(4);
    p->next->next->next->next = new ListNode(5);
    p->next->next->next->next->next = nullptr;
    Solution s;

    ListNode *head = p;
    s.reverse(p, 3);
    cout<<(head->val)>>endl;
    return 0;
}
