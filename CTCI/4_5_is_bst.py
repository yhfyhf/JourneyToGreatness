from utils import TreeNode, array2bst



def is_bst(root):
    if not root:
        return True
    flag = True
    if root.left:
        flag = flag and root.left.val < root.val
    if root.right:
        flag = flag and root.right.val > root.val
    if not flag:
        return False
    else:
        return is_bst(root.left) and is_bst(root.right)


    
    

if __name__ == '__main__':
    array = [i for i in xrange(15)]
    tree = array2bst(arr)
    print is_bst(tree)