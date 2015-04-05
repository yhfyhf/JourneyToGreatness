# Tree专题
## 二叉树的遍历
PreOrder(T) = T的根结点 + PreOrder(T左子树) + PreOrder(T右子树)

InOrder(T) = InOrder(T左子树) + T的根结点 + InOrder(T右子树)

PostOrder(T) = PostOrder(T左子树) + PostOrder(T右子树) + T的根结点

如图：

![](http://i.imgur.com/u8y6ABf.png)

PreOrder: 4,2,1,3,5,6,7

InOrder: 1,2,3,4,5,7,6

PostOrder: 1,3,2,7,6,5,4

InOrder：一个结点前驱是其左子树最右下角节点，后继是右子树最左下角的节点

PostOrder:
(1)若一结点是根，无后继;
(2)若一结点是parent的右子树(3是2的右子树)，或者是左子树但无右子树(6下有7)，后继为parent;
(3)结点是左子树且parent的右子树存在，后继为右子树后序遍历的第一个结点。

## 对比树
``` python
def compareTree(root1, root2):
    # @param root1, the root Node of a tree
    # @param root2, the root Node of another tree
    # @return True or False
    if not root1 and not root2:
        return True
    if root1 and not root2:
        return False
    if root2 and not root1:
        return False
    # Careful, if one is str and other is int, would be false
    if str(root1.val) != str(root2.val):
        return False
    return compareTree(root1.left, root2.left) and \
        compareTree(root1.right, root2.right)


```
## 重建树
+ Given PreOrder and InOrder，rebuild tree
+ Given PostOrder and InOrder, rebuild tree
+ Warning, Given PreOrder and PostOrder, we cannot rebuild the tree because PreOrder and PostOrder only identify the relationship of parent and children. Only InOrder tells the information of left child and right children.

``` python
def rebuild1(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Node(inorder[0])
    root = Node(postorder[-1])
    p = inorder.index(postorder[-1])
    root.left = rebuild1(inorder[:p], postorder[:p])
    root.right = rebuild1(inorder[p+1:], postorder[p:-1])
    return root
```

``` python
def rebuild2(preorder, inorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Node(inorder[0])
    root = Node(preorder[0])
    p = inorder.index(preorder[0])
    root.left = rebuild2(preorder[1:p+1], inorder[:p])
    root.right = rebuild2(preorder[p+1:], inorder[p+1:])
    return root

```

## BST
+ Construct BST from sorted array

> 1) Get the Middle of the array and make it root.

> 2) Recursively do same for left half and right half

      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.

## Tries


## 思想
递归的看问题
凡是写不止一遍的检查，都可以抽象在上层只写一遍
Edge Case for None

## TODO
+ **Minimum Depth of Binary Tree ** in BFS
