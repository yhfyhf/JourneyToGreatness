#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
	// http://articles.leetcode.com/2010/10/binary-tree-post-order-traversal.html
        stack<TreeNode *> s;
        vector<int> res;
        TreeNode *prev = nullptr;
        if (root)
            s.push(root);
        while (!s.empty()) {
	    // 这里不pop
            TreeNode *curr = s.top();
	    // prev == nullptr不能忘记，一开始！
            if (prev == nullptr || prev->left == curr || prev->right == curr) {
                if (curr->left) 
                    s.push(curr->left);
                else if (curr->right)
                    s.push(curr->right);
            }
            else if (prev == curr->left) {
                if (curr->right)
                    s.push(curr->right);
            }
	    // 两种情况走到这，1）前一次循环满足前两个大条件中的一个，但是内部小条件都不满足，说明需要输出了，prev == curr，本次来到这。
	    // 本次是 prev == curr->right
            else {
                res.push_back(curr->val);
                s.pop();
            }
            prev = curr;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
