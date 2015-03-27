#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    void flatten(TreeNode *root) {
        if (!root)
            return ;
        flatten(root->left);
        flatten(root->right);
        
        if (!root->left) return;
        
        TreeNode *p = root->left;
        while(p->right) p = p->right;
        p->right = root->right;
        root->right = root->left;
        root->left = nullptr;
    }

    void flatten2(TreeNode * root) {
	
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
