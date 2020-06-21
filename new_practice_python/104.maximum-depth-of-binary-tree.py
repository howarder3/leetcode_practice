#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    def maxDepth(self, root):
        if root is None:
            return 0

        level_cnt = 0
        level = [root]

        while level:
            level_cnt += 1

            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:
                    next_level.append(ele.right)
                
            level = next_level

        return level_cnt


        

    

        

# @lc code=end

