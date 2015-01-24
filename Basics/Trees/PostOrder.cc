/*
 * The code below are from soulmachine
 * https://github.com/soulmachine/acm-cheat-sheet/blob/a423cc8045da3721e560f4fe86d66ea896a2bb8c/C%2B%2B/chapTree.tex
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

/* ---------- Gvien preorder and inorder, just print postorder ---------- */

/**
 * @brief 给定前序遍历和中序遍历，输出后序遍历.
 *
 * @param[in] pre 前序遍历的序列
 * @param[in] in 中序遍历的序列
 * @param[in] n 序列的长度
 * @param[out] post 后续遍历的序列
 * @return 无
 */
void build_post(const char * pre, const char *in, const int n, char *post) {
    int left_len = strchr(in, pre[0]) - in;
    if(n <= 0) return;
    
    build_post(pre + 1, in, left_len, post);
    build_post(pre + left_len + 1, in + left_len + 1,
			   n - left_len - 1, post + left_len);
    post[n - 1] = pre[0];
}

#define MAX  64
// 测试
// BCAD CBAD，输出 CDAB
// DBACEGF ABCDEFG，输出 ACBFGED
void build_post_test() {
    char pre[MAX] = {0};
    char in[MAX] = {0};
    char post[MAX] = {0};
    int n;

    scanf("%s%s", pre, in);
    n = strlen(pre);

    build_post(pre, in, n, post);
    printf("%s\n", post);
}








/* ---------- Rebuild the tree physically ---------- */


/* 结点数据的类型. */
typedef char elem_t;

/**
 *@struct
 *@brief 二叉树结点.
 */
typedef struct bt_node_t {
    elem_t elem; /* 节点的数据 */
    struct bt_node_t *left; /* 左孩子 */
    struct bt_node_t *right; /* 右孩子 */
} bt_node_t;

/**
 * @brief 给定前序遍历和中序遍历，重建二叉树.
 *
 * @param[in] pre 前序遍历的序列
 * @param[in] in 中序遍历的序列
 * @param[in] n 序列的长度
 * @param[out] root 根节点
 * @return 无
 */
void rebuild(const char *pre, const char *in, int n, bt_node_t **root) {
    int left_len;
    // 检查终止条件
    if (n <= 0 || pre == NULL || in == NULL)
        return;
    //获得前序遍历的第一个结点
    *root = (bt_node_t*) malloc(sizeof(bt_node_t));
    (*root)->elem = *pre;
    (*root)->left = NULL;
    (*root)->right = NULL;

    left_len = strchr(in, pre[0]) - in;
    //重建左子树
    rebuild(pre + 1, in, left_len, &((*root)->left));
    //重建右子树
    rebuild(pre + left_len + 1, in + left_len + 1, n - left_len - 1,
            &((*root)->right));
}

void print_post_order(const bt_node_t *root) {
    if(root != NULL) {
        print_post_order(root->left);
        print_post_order(root->right);
        printf("%c", root->elem);
    }
}

void rebuild_test() {
    char pre[MAX] = { 0 };
    char in[MAX] = { 0 };
    int n;
    bt_node_t *root;
    scanf("%s%s", pre, in);
    n = strlen(pre);
    
    rebuild(pre, in, n, &root);
    print_post_order(root);
}

int main() {
    build_post_test();
    // rebuild_test();
    return 0;
}
