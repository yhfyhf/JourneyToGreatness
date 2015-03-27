#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast = head, *slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if ( fast == slow) {
                return true;
            }
        }
        return false;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
