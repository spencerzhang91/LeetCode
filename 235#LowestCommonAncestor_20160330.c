// 235 Lowest Common Ancestor of BST

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q)
{
     while (root)
     {
        switch (helper(root->val, p->val, q->val))
        {
            case -1: root = root->left;
                     lowestCommonAncestor(root, p, q);
                     break;
            case  1: root = root->right;
                     lowestCommonAncestor(root, p, q);
                     break;
            case  0: return root;
        }
     }
     return NULL;
}

int helper(int pivot, int a, int b)
{
    if (a < pivot && b < pivot)
        return -1;
    else if (a > pivot && b > pivot)
        return 1;
    else return 0;
}