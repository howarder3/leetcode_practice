/*
 * @lc app=leetcode id=101 lang=cpp
 *
 * [101] Symmetric Tree
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

//  struct TreeNode{
//      int val;
//      TreeNode *left;
//      TreeNode *right;
//      TreeNode(): val(0), left(NULL), right(NULL){}
//      TreeNode(int x): val(x), left(NULL), right(NULL){}
//      TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
//  }

class Solution {
public:
    // sol3
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;

        return helper(root->left, root->right);
        
    }

    bool helper(TreeNode *p, TreeNode *q){
        if(!p && !q){return true;}
        else if(!p || !q){return false;}

        if(p->val != q->val){return false;}

        return helper(p->left, q->right) && helper(p->right, q->left);
    }

        // sol2
        // if(!root) return true;
        
        // queue<TreeNode*> check;

        // check.push(root->left);
        // check.push(root->right);

        // while(!check.empty()){
        //     TreeNode* node1 = check.front();
        //     check.pop();
        //     TreeNode* node2 = check.front();
        //     check.pop();

        //     if(!node1 && node2){return false;}
        //     if(!node2 && node1){return false;}
        //     if(node1 && node2){
        //         if(node1->val != node2->val)
        //             return false;
        //         check.push(node1->left);
        //         check.push(node2->right);

        //         check.push(node1->right);
        //         check.push(node2->left);
        //     }
        // }
        // return true;
          


        // https://leetcode.com/problems/symmetric-tree/discuss/33089/My-C%2B%2B-Accepted-code-in-16ms-with-iteration-solution
        // TreeNode *left, *right;
        // if(!root)
        //     return true;

        // queue<TreeNode *> q1,q2;
        // q1.push(root->left);
        // q2.push(root->right);
        // while(!q1.empty() && !q2.empty()){
        //     left = q1.front();
        //     q1.pop();
        //     right = q2.front();
        //     q2.pop();
        //     if(left == NULL && right == NULL)
        //         continue;
        //     if(left == NULL || right == NULL)
        //         return false;
        //     if(left->val != right->val)
        //         return false;
            
        //     q1.push(left->left);
        //     q1.push(left->right);
            
        //     q2.push(right->right);
        //     q2.push(right->left);
        // }

        // return true; 
    // }
};
// @lc code=end

