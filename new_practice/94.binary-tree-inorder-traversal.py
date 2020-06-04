#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# : TreeNode) -> List[int]

class Solution:
    def inorderTraversal(self, root):
        # iteratively 

        # inorder: l, root, r
        res, stack = [], []
        while True:
            while root: # if have something (in left)
                stack.append(root)
                root = root.left # (1) go left first(deeper)

            if not stack: # nothing in stack
                return res
            
            node = stack.pop() ## last root(node) pop
            res.append(node.val) ## (2) add value
            root = node.right # (3) go right (deeper)

    #    # recursively
    #     res = []
    #     self.helper(root, res) ## start from root
    #     return res

    # def helper(self, root, res):
    #     if root: ## if have something (if no then pass)
    #         self.helper(root.left, res)
    #         res.append(root.val)
    #         self.helper(root.right, res)







# @lc code=end

