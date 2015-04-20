#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        vector<TreeLinkNode*> curr, next;
        if (!root)
            return;
        curr.push_back(root);
        while (!curr.empty()) {
            next.clear();
            if (curr.size() == 1) {
                curr[0]->next = nullptr;
            } else {
                for (int i = 1; i < curr.size(); i++) {
                    curr[i-1]->next = curr[i];
                }
                curr.back()->next = nullptr;
            }
            for (auto node: curr) {
                if (node->left)
                    next.push_back(node->left);
                if (node->right)
                    next.push_back(node->right);
            }
            curr = next;
        }
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
