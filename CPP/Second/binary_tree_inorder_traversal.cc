// https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

// Given a binary tree, return the inorder traversal of its nodes' values.
// For example:
// Given binary tree {1,#,2,3},
//    1
//     \
//      2
//     /
//    3
// return [1,3,2].
// Note: Recursive solution is trivial, could you do it iteratively?
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

/*
  http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
  1) Create an empty stack S.
  2) Initialize current node as root
  3) Push the current node to S and set current = current->left until current is NULL
  4) If current is NULL and stack is not empty then 
       a) Pop the top item from stack.
       b) Print the popped item, set current = popped_item->right 
       c) Go to step 3.
  5) If current is NULL and stack is empty then we are done.
 */

class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        stack<TreeNode *> s;
        vector<int> res;
        TreeNode *p = root;
	//必须两个条件任一满足
        while (!s.empty() || p) {
            if (p != nullptr) {
                s.push(p);
                p = p->left;
            }
            else {
                p = s.top();
                s.pop();
                res.push_back(p->val);
                p = p->right;
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
