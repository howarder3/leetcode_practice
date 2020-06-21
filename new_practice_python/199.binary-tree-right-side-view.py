#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    def rightSideView(self, root):

        if not root:
            return []

        
        level = [root]
        ans = []

        while level:
            ans.append(level[-1].val)

            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:
                    next_level.append(ele.right)

            level = next_level

        return ans








        
# @lc code=end

