#include <vector>
#include <queue>
#include <iostream>


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
    static std::vector<int> rightSideView(TreeNode* root) {
        if (!root) return std::vector<int>{};

        std::queue<TreeNode*> frontier{};
        std::vector<int> ret{};

        ret.push_back(root->val);

        TreeNode* rightSide{};
        frontier.push(root);
        frontier.push(nullptr);
        
        while (frontier.size() > 1) {
            TreeNode* curr = frontier.front();
            frontier.pop();

            if (curr == nullptr) {
                ret.push_back(rightSide->val);
                frontier.push(nullptr);
                continue;
            }

            if (curr->left != nullptr) {
                frontier.push(curr->left);
                rightSide = curr->left;
            }
            
            if (curr->right != nullptr) {
                frontier.push(curr->right);
                rightSide = curr->right;
            }
        }

        return ret;
    }
};

int main() {
    TreeNode* root = new TreeNode{};

    std::cout << Solution::rightSideView(root)[0] << "\n";
}