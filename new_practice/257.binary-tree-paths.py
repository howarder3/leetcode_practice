#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    def binaryTreePaths(self, root):
        if not root:
            return []

        ans = []
        self.dfs(root, "", ans)

        return ans


    def dfs(self, root, path, ans):
        if not root:
            return 

        if root.left is None and root.right is None: # checked leaf
            ans.append(path+str(root.val))
            return

        self.dfs(root.left, path+str(root.val)+"->", ans)
        self.dfs(root.right, path+str(root.val)+"->", ans)

        


# @lc code=end

