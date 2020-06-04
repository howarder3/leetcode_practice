#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def flatten(self, root: TreeNode) -> None:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        val_array = []
        self.preorder(root, val_array)
        # print(val_array)
        self.buildTree(root, val_array)

    def preorder(self, root, val_array):
        # V LR
        if not root:
            return

        val_array.append(root.val)
        self.preorder(root.left, val_array)
        self.preorder(root.right, val_array)

    def buildTree(self, root, val_array):
        if not val_array:
            return


        # a = b = 0
        # b = b+1
        # print(a,b) # 0 1

        # V = val_array.pop(0)
        # root = n = TreeNode(V)

        # root = TreeNode(V) 
        # n = root
        # n.left = None
        # while(val_array):
        #     V = val_array.pop(0)
        #     n.right = TreeNode(V)
        #     n = n.right
        #     n.left = None
        
        # root.left = None # change in-place
        # root.right = TreeNode(val_array.pop(0))  # change in-place
        # dont need at least 1, 不用至少需要一個
        val_array.pop(0) # same root, first pop


        while(val_array):
            root.left = None # change in-place
            root.right = TreeNode(val_array.pop(0)) # change in-place
            root = root.right
            
            
        # print(root)
        

        
# @lc code=end

