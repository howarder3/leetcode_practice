#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    # def hasPathSum(self, root, sum):

        
    #     if not root: # 到底了 
    #         if sum == 0:
    #             return True
    #         else:
    #             return False 

    #     # if sum == 0: # 沒到底就有?
    #         # return True


    #     return self.hasPathSum(root.left, sum-root.val) or \
    #         self.hasPathSum(root.right, sum-root.val)

    # https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
    def hasPathSum(self, root, sum):
        if not root:
            return False

        # ([], 0) case

        if not root.left and not root.right and root.val == sum: # 確保沒有另一邊
            return True

        # ([1, 2], 1) case

  
        return self.hasPathSum(root.left, sum-root.val) or \
            self.hasPathSum(root.right, sum-root.val)






# @lc code=end

