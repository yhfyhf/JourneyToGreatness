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
private:
    void connect(TreeLinkNode *root, TreeLinkNode *sib) {
        if (!root)
            return;
        else
            root->next = sib;
        connect(root->left, root->right);
        if (sib)
            connect(root->right, sib->left);
        else
            connect(root->right, nullptr);
    }
public:
    void connect(TreeLinkNode *root) {
        connect(root, nullptr);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
