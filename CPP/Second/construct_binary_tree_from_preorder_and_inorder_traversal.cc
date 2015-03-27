// https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

// Given preorder and inorder traversal of a tree, construct the binary tree.
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

/*
    Time O(n), Space O(logN)
*/

class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return build(&preorder[0], &*preorder.end(), &inorder[0], &*inorder.end());
    }
    
    TreeNode* build(int *pb, int *pe, int *ib, int *ie) {
        if (pb == pe)
            return nullptr;
        auto root = new TreeNode(*pb);
        int left_len = find(ib, ie, root->val) - ib;
        root->left = build(pb+1, pb+1+left_len, ib, ib+left_len);
        root->right = build(pb+1+left_len, pe, ib+left_len+1, ie);
        return root;
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
