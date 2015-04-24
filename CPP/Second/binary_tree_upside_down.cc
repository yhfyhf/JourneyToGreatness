#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution() {
 public:
    TreeNode UpsideDownBinaryTree(TreeNode root) {
	return bottomup(root, nullptr);
    }
 private:
    TreeNode bottomup(TreeNode p, TreeNode parent) {
	if (!p)
	    return parent;
	TreeNode root = bottomup(p.left, p);
	p.left = (parent == nullptr) ? parent : parent.right;
	p.right = parent;
	return root;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
