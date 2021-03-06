/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:


	
    TreeNode *sortedListToBST(ListNode *head) {
		int len = 0;
		ListNode *node = head;
		while (node != NULL) {
			node = node->next;
			len++;
		}
		return build(head, 0, len-1);
		}
	
	TreeNode *build(ListNode *&node, int start, int end) {
		if (start > end)
			return NULL;
		int mid = start + (end - start)/2;
		TreeNode *left = build(node, start, mid-1);
		TreeNode *root = new TreeNode(node->val);
		root->left = left;
		node = node->next;
		root->right = build(node, mid+1, end);
		return root;
    }
};
