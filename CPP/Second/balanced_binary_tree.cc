#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
  好剪枝
*/

class Solution {
public:
    int height(TreeNode * root) {
        if (! root)
            return 0;
        int left = height(root->left);
        int right = height(root->right);
	// abort caculation, 向上传失败信息
        if (left < 0 || right < 0 || abs(left-right) > 1)
            return -1;
        return max(left, right) + 1;    
    }
    
    bool isBalanced(TreeNode *root) {
        return height(root) >= 0;
    }

    int height2(TreeNode * root) {
        if (! root)
            return 0;
        int left = height(root->left);
	if (left < 0)
	    return -1;
        int right = height(root->right);
	// abort caculation, 向上传失败信息
        if (right < 0 || abs(left-right) > 1)
            return -1;
        return max(left, right) + 1;    
    }
    
    
};



int main(int argc, char *argv[])
{

    return 0;
}
