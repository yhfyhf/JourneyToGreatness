#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode *root) {
        vector<int> res;
        vector<TreeNode*> curr, next;
        if (!root)
            return res;
        curr.push_back(root);
        while(!curr.empty()) {
            res.push_back(curr.back()->val);
            next.clear();
            for (auto node : curr) {
                if (node->left)
                    next.push_back(node->left);
                if (node->right)
                    next.push_back(node->right);
            }
            curr = next;
        }
        return res;
    }
};


