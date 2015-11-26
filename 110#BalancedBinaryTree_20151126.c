/* 110#BalancedBinaryTree */
/* Definition for a binary tree node. */

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


#define MAX(x, y) (((x)>(y))? (x): (y))

bool isBalanced(struct TreeNode *root)
{
    if (!root)
        return true;
    else if (isBalanced(root->left) && isBalanced(root->right) &&
        diff(treeDepth(root->left), treeDepth(root->right)) <= 1)
        return true;
    else
        return false;
}

int treeDepth(struct TreeNode *root)
{
    if (!root)
        return 0;
    return MAX((treeDepth(root->left) + 1), (treeDepth(root->right) + 1));
}

int diff(int d1, int d2)
{
    if (d1 > d2) return d1 - d2;
    else return d2 - d1;
}
