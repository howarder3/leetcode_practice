#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    # def isBalanced(self, root):
    #     if not root:
    #         return True


    #     # print(self.height(root))
    #     if self.height(root) == -1:
    #         return False

    #     return True





    # def height(self, root):
    #     if not root:
    #         return 1

    #     height_left = self.height(root.left)
    #     height_right = self.height(root.right)
        
    #     if height_left == -1 or height_right == -1:
    #         return -1
    #     elif abs(height_left - height_right) > 1:
    #         return -1
    #     else:
    #         height = max(height_left, height_right) + 1

    #     return height

    # https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
    def isBalanced(self, root):
        if not root:
            return True

        return self.height(root)[1]



    def height(self, root): # return (height, bool)
        if not root:
            return (1, True)

        if self.height(root.left)[1] and self.height(root.left)[1]: # if all True
            height_l = self.height(root.left)[0]
            height_r = self.height(root.right)[0]

            if abs(height_l - height_r) > 1:
                return (-1, False)
            else:
                return (max(height_l, height_r)+1, True)
        else: # any False
            return (-1, False)

                
# @lc code=end

