#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        stack<TreeNode *> s;
        vector<int> res;
        TreeNode *p;
        p = root;
        if (p != nullptr)
            s.push(p);
            
        while(!s.empty()) {
            p = s.top();
            s.pop();
            res.push_back(p->val);
            
            if (p->right)
                s.push(p->right);
            if (p->left)
                s.push(p->left);
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
