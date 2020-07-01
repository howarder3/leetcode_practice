/*
 * @lc app=leetcode id=102 lang=cpp
 *
 * [102] Binary Tree Level Order Traversal
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
    vector<vector<int>> levelOrder(TreeNode* root) {

        if(!root) return {};

        vector<vector<int>> ans = {};
        vector<TreeNode*> level = {root};

        while(!level.empty()) {
            vector<int> ans_level = {};
            for(int i = 0; i < level.size(); i++){
                // cout<<level[i]->val;
                ans_level.push_back(level[i]->val);
            }
            ans.push_back(ans_level);


            vector<TreeNode*> next_level = {};

            for(int i = 0; i < level.size(); i++){
                if(level[i]->left) // something
                    next_level.push_back(level[i]->left);
                if(level[i]->right) // something
                    next_level.push_back(level[i]->right);
            }
            level = next_level;
        }
        return ans;
    }
};
// @lc code=end

