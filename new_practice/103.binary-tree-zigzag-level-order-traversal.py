#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    def zigzagLevelOrder(self, root):  

        ans = []
        level = [root]
        Zigzag = True

        if root is None:
            return []

        while level:
            # add new level
            ans_temp = []
            for ele in level:
                ans_temp.append(ele.val)


            if Zigzag:
                ans.append(ans_temp)
            else:
                ans.append(ans_temp[::-1])

            Zigzag = not Zigzag

            # find next Level
            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:   
                    next_level.append(ele.right)

            level = next_level

        return ans


        
# @lc code=end

