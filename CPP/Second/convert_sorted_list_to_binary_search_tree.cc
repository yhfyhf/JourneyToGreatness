#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        if (! head)
            return nullptr;
        ListNode *mid = head, *fast = head, *prev = nullptr;
        while(fast->next && fast->next->next) {
            prev = mid;
            mid = mid->next;
            fast = fast->next->next;
        }
        TreeNode *root = new TreeNode(mid->val);
        if (prev) {
            prev->next = nullptr;
            root->left = sortedListToBST(head);
        }
        root->right = sortedListToBST(mid->next);
        return root;
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
