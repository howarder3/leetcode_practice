#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return 
        if not inorder:
            return 


        # find V(preorder:V LR), use inorder(L V R) 

        V = preorder.pop(0)
        root = TreeNode(V)

        idx_of_V_inorder = inorder.index(V)
        root.left = self.buildTree(preorder ,inorder[:idx_of_V_inorder])
        root.right = self.buildTree(preorder ,inorder[idx_of_V_inorder+1:])

        return root




# @lc code=end

