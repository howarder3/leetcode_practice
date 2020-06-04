#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    # def isValidBST(self, root):
    #     if root is None:
    #         return True

    #     checked_down_left = self.isValidBST(root.left)
    #     checked_down_right = self.isValidBST(root.right)


    #     if root.left is None or root.val > root.left.val:
    #         checked_left = True
    #     else:
    #         checked_left = False
            


    #     if root.right is None or root.val < root.right.val:
    #         checked_right = True
    #     else:
    #         checked_left = False


    #     return checked_down_left and checked_down_right and checked_left and checked_down_right

    def isValidBST(self, root): 
        if root is None:
            return True

        output = []
        self.inorder(root, output)
        print(output)

        output = []
        self.preorder(root, output)
        print(output)

        output = []
        self.postorder(root, output)
        print(output)

        output = []
        self.levelorder(root, output)
        print(output)




    def inorder(self, root, output): # L V R
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


    def preorder(self, root, output): # V LR
        if root is None:
            return

        output.append(root.val)
        self.inorder(root.left, output)        
        self.inorder(root.right, output)

    def postorder(self, root, output): # LR V
        if root is None:
            return

        self.inorder(root.left, output)        
        self.inorder(root.right, output)
        output.append(root.val)

    def levelorder(self, root, output): # LR V
        if root is None:
            return

        level = [root]


        while level:

            ans_temp = [] 
            for ele in level:
                ans_temp.append(ele.val)

            output.append(ans_temp)

            # find next level
            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:
                    next_level.append(ele.right)    

            level = next_level

        
# @lc code=end

