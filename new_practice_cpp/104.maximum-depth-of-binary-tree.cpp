/*
 * @lc app=leetcode id=104 lang=cpp
 *
 * [104] Maximum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int current_max = 0;
        helper(root, current_max, 0);
        return current_max;
    }

    void helper(TreeNode* root, int& current_max, int current_depth){
        if(!root){
            current_max = max(current_max, current_depth);
            // cout<<current_depth;
            return;
        }

        helper(root->left, current_max, current_depth+1);
        helper(root->right, current_max, current_depth+1);
    }
};
// @lc code=end

