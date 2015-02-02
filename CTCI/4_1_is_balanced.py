from utils import TreeNode

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def is_balanced(root):
    if root is None:
        return True
    if abs(height(root.left) - height(root.right)) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)
    else:
        return False

def depth(root):
    if root is None:
        return 0
    else:
        if hasattr(root, 'depth'):
            return root.depth
        else:
            root.depth = 1 + max(depth(root.left), depth(root.right))
            return root.depth

def is_balanced2(root):
    return check_balanced_helper(root)[0]
def check_balanced_helper(root):
    """
    check balance and caculate height at the same time
    """
    # @return (isBalance, depth): in type of boolean and it
    if root is None:
        return True, 0
    left_balanced, left_height = check_balanced_helper(root.left)
    right_balanced, right_height = check_balanced_helper(root.right)
    root.depth = 1 + max(left_height, right_height)
    return left_balanced and right_balanced and \
        (abs(depth(root.left) - depth(root.right)) <= 1), root.depth
    
if __name__ == '__main__':
    l = TreeNode(3, TreeNode(1), TreeNode(2))
    r = TreeNode(5, left = TreeNode(6))
    root = TreeNode(5, l, r)
    print is_balanced(root)