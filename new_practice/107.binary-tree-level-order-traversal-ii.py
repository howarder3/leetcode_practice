#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    def levelOrderBottom(self, root):

        ans = []
        level = [root]

        if root is None:
            return []

        while level:
            # add value 
            ans_temp = []
            for ele in level:
                ans_temp.append(ele.val)

            ans.append(ans_temp)

            # find next level
            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:
                    next_level.append(ele.right)

            level = next_level
            


        return ans[::-1]


        
# @lc code=end

