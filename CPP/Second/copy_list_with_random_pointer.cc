#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (!head)
            return nullptr;
        RandomListNode *old = head, *nw;
        // copy linkedlist's each node
        while(old) {
            nw = new RandomListNode(old->label);
            nw->next = old->next;
            old->next = nw;
            old = nw->next;
        }
        // copy random pointers
        old = head;
        while(old) {
            nw = old->next;
            // some node's random is none
            if (old->random)
                nw->random = old->random->next;
            old = nw->next;
        }
        // detach two lists
        RandomListNode *new_head = head->next;
        old = head;
        while (old) {
            nw = old->next;
            old->next = nw->next;
            // in case of the last one
            if (nw->next)
                nw->next = nw->next->next;
            old = old->next;
        }
        return new_head;
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
