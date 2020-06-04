#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTree(self, inorder, postorder):
        # inorder LVR
        # postorder LR V

        if not inorder: # nothing
            return
        if not postorder: # nothing
            return

        # [] has something!!!!!

        # print("inorder:",inorder)
        # print("postorder:",postorder)

        # print(postorder)
        V = postorder.pop()
        # postorder is not None -> len(postorder) > 0
        
        # print(V)
        # print((V not in inorder))
        # print((not postorder))
        # while((V not in inorder) and (postorder)): # TT 才做, postorder 有東西才做
        #     V = postorder.pop()
            # print(V)

        idx_of_V_inorder = inorder.index(V)
        root = TreeNode(V)
        # postorder2 = postorder.copy()

        # print("postorder_left:",postorder)
        # root.left = self.buildTree(inorder[:idx_of_V_inorder], postorder)
        # # print("postorder_right:",postorder)
        # root.right = self.buildTree(inorder[idx_of_V_inorder+1:], postorder)


        # see right first!!!! (because LR <- V) see R first, R first pop

        # print("postorder_left:",postorder)
        root.right = self.buildTree(inorder[idx_of_V_inorder+1:], postorder)
        root.left = self.buildTree(inorder[:idx_of_V_inorder], postorder)
        # # print("postorder_right:",postorder)
        

        return root


        # https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
        # see right first!!!! (because LR <- V) see R first, R first pop
        
        
# @lc code=end

