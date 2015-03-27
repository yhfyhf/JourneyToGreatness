// https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

// Given inorder and postorder traversal of a tree, construct the binary tree.
// Note:
// You may assume that duplicates do not exist in the tree.

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return build(&inorder[0], &*inorder.end(), &postorder[0], &*postorder.end());
    }
    
    TreeNode *build(int *ib, int *ie, int *pb, int * pe) {
        if (ib == ie)
            return nullptr;
        auto root = new TreeNode(pe[-1]);
        int left_len = find(ib, ie, pe[-1]) - ib;
        root->left = build(ib, ib+left_len, pb, pb+left_len);
        root->right = build(ib+left_len+1, ie, pb+left_len, pe-1);
        return root;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
