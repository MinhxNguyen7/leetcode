struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

 
class Solution {
public:
    int goodNodes(TreeNode* root, const int maxParent = -10000);
};

int Solution::goodNodes(TreeNode* root, const int maxParent) {
    if (!root) return 0;
    
    const int newMax = maxParent >= root->val ? maxParent : root->val;

    const bool isGood = root->val >= maxParent;

    return isGood + goodNodes(root->left, newMax) + goodNodes(root->right, newMax);
};
