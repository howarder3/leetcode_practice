/*
 * @lc app=leetcode id=103 lang=cpp
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {

        if(!root) return {};

        vector<vector<int>> ans;
        vector<TreeNode*> level = {root};
        bool zigzag = true;

        while(!level.empty()){

            vector<int> ans_level = {};
            if(zigzag){
                for(int i = 0;i< level.size();i++)
                    ans_level.push_back(level[i]->val);
            }
            else{
                for(int i = level.size()-1;i>=0;i--)
                    ans_level.push_back(level[i]->val);
            }
            zigzag = !zigzag;
            ans.push_back(ans_level);

            vector<TreeNode*> next_level = {};
            for(int i = 0;i< level.size();i++){
                if(level[i]->left) // if exists
                    next_level.push_back(level[i]->left); 
                if(level[i]->right) // if exists
                    next_level.push_back(level[i]->right); 
            }
            level = next_level;
        }
        return ans;
    }
};
// @lc code=end

