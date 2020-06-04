#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    def pathSum(self, root, sum):
        if not root:
            return []

        ans = []
        self.dfs(root, [], ans, sum)

        return ans

    def dfs(self, root, path, ans, mysum):
        if not root: # case = [1,2]
            return


        # print(path)
        # case = [1,2], need check if right or left has something
        if (sum(path) + root.val == mysum) and (root.left is None) and (root.right is None):
            ans.append(path + [root.val])
            return       

        # early return, don't do it!!!! if minus!!!!
        # if sum(path) + root.val > mysum:
        #     return

        # path.append(root.val) # can not use append, change the list!!!
        self.dfs(root.left, path + [root.val], ans, mysum)
        self.dfs(root.right, path + [root.val], ans, mysum)


        # can not use append, change the list!!!

# 0. can not use append, will change the list!!!
# 1. case = [1,2], need check if right or left has something
# 2. early return, don't do it!!!! if minus!!!!
        




        
# @lc code=end

