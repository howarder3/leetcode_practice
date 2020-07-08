/*
 * @lc app=leetcode id=199 lang=cpp
 *
 * [199] Binary Tree Right Side View
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


// level order
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if(!root)
            return {};
            
        vector<int> ans;
        vector<TreeNode*> level_nodes;
        level_nodes.push_back(root);

        while(!level_nodes.empty()) {
            ans.push_back(level_nodes[level_nodes.size()-1]->val); // push ans

            vector<TreeNode*> next_level;
            for(int i=0; i<level_nodes.size();i++){
                if(level_nodes[i]->left!=NULL)
                    next_level.push_back(level_nodes[i]->left);
                if(level_nodes[i]->right!=NULL)
                    next_level.push_back(level_nodes[i]->right);
            }

            level_nodes = next_level;
        }
        return ans;
    }
};
// @lc code=end

