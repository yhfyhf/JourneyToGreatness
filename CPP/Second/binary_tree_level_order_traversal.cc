// https://oj.leetcode.com/problems/binary-tree-level-order-traversal/

// Given a binary tree, return the level order traversal of its nodes' values.
// For example:
// Given binary tree {3,9,20,#,#,15,7},
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//   [3],
//   [9,20],
//   [15,7]
// ]
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
    vector<vector<int> > levelOrder(TreeNode *p) {
        vector<vector<int> > res;
	if (!p)
	    return res;
	vector<TreeNode *> cur;
	cur.push_back(p);
	while (!cur.empty()) {
	    vector<int> tmp;
	    for(auto e: cur)
		    tmp.push_back(e->val);
	    res.push_back(tmp);
	    vector<TreeNode *> next;
	    for (auto e: cur) {
		if (e->left)
		    next.push_back(e->left);
		if (e->right)
		    next.push_back(e->right);
	    }
	    cur = next;
	}
	return res;
    }

    vector<vector<int> > levelOrder2(TreeNode *p) {
	vector<vector<int> > res;
	traverse(root, 0, res);
	return res
    }
    void traverse(TreeNode *root, size_t level, vector<vector<int> > &res) {
	if (! root)
	    return;
	if (level > res.size() - 1)
	    res.push_back(vector<int>);
	res[level].push_back(root->val); // res.back().push_back(root->val);
	traverse(root->left, level + 1, res);
	traverse(root->right, level + 1, res);	
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
