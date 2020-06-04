#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TreeNode, k: int) -> int:

class Solution:
    # Python Easy Iterative and Recursive Solution
    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution

    # Recursive:
    # def kthSmallest(self, root, k):
    #     self.k = k
    #     self.res = None
    #     self.helper(root)
    #     return self.res

    # def helper(self, node):
    #     if not node:
    #         return
    #     self.helper(node.left)
    #     self.k -= 1
    #     if self.k == 0:
    #         self.res = node.val
    #         return
    #     self.helper(node.right)

    # Iterative:
    def kthSmallest(self, root, k): 
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        





# @lc code=end

