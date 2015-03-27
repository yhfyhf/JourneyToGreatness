// https://oj.leetcode.com/problems/symmetric-tree/

// Given a binary tree, check whether it is a mirror of itself (ie, symmetric
// For example, this binary tree is symmetric:
//     1
//    / \
//   2   2
//  / \ / \
// 3  4 4  3
// But the following is not:
//     1
//    / \
//   2   2
//    \   \
//    3    3
// Note:
// Bonus points if you could solve it both recursively and iteratively.
// confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
// OJ's Binary Tree Serialization:
// The serialization of a binary tree follows a level order traversal, where '#'
// Here's an example:
//    1
//   / \
//  2   3
//     /
//    4
//     \
//      5
// The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

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
    bool isSym(TreeNode *p, TreeNode * q) {
        if (!p && !q)
            return true;
        if (!p || !q)
            return false;
        if (p->val != q->val)
            return false;
        return isSym(p->left, q->right) && isSym(p->right, q->left);
    }
    
    bool isSymmetric(TreeNode *root) {
        if (!root)
            return true;
        return isSym(root->left, root->right);
    }
   
};

int main(int argc, char *argv[])
{

    return 0;
}
