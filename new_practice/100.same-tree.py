#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None: # 只有一個None
            return False

        if p.val == q.val:
            check_left = self.isSameTree(p.left, q.left)
            check_right = self.isSameTree(p.right, q.right)
        else:
            return False
        
        return check_left and check_right



# @lc code=end

