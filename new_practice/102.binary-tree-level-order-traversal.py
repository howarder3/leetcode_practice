#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def levelOrder(self, root: TreeNode) -> List[List[int]]:

# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
class Solution:
    # def levelOrder(self, root):
        # ans, level = [], [root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     print("ans:", ans)
        #     LRpair = [(node.left, node.right) for node in level]
        #     print("LRpair:", LRpair)
        #     level = [leaf for LR in LRpair for leaf in LR if leaf]
        #     print("level:", level)
        # return ans



    # def levelOrder(self, root):
    #     ans, level = [], [root]

    #     while root and level:
    #         # 處理 ans
    #         ans_temp = []
    #         for node in level:
    #             ans_temp.append(node.val)
    #         ans.append(ans_temp)
    #         print("ans:", ans)

    #         # LRpair
    #         LRpair = []
    #         for node in level:
    #             LRpair.append((node.left, node.right))
    #         print("LRpair:", LRpair)

    #         # next level
    #         level = []
    #         for LR in LRpair:
    #             for leaf in LR:
    #                 if leaf:
    #                     level.append(leaf)
    #         print("level:", level)
    #         # if level is None, next while ends 

    #     return ans

    # def levelOrder(self, root):
    #     ans, level = [], [root]
    #     while root and level:
    #         # ans.append([node.val for node in level])            
    #         # level = [kid for n in level for kid in (n.left, n.right) if kid]

    #         ans_temp = []
    #         # collect val
    #         for node in level:
    #             ans_temp.append(node.val)

    #         ans.append(ans_temp)

    #         # next level
    #         next_level = []
    #         for n in level:
    #             for kid in (n.left, n.right):
    #                 if kid:
    #                     next_level.append(kid)

    #         level = next_level

    #     return ans

    # def levelOrder(self, root):
    #     if not root: # nothing have
    #         return []
    #     ans, level = [], [root]

    #     while level: # 如果下層還有剩

    #         ans_temp = []
    #         for node in level:
    #             ans_temp.append(node.val)
            
    #         ans.append(ans_temp)


    #         # find all next level
    #         temp = []
    #         for node in level:
    #             temp.append(node.left)
    #             temp.append(node.right)
            
    #         level = [] # count next_level nodes
    #         for leaf in temp:
    #             if leaf:
    #                 level.append(leaf)
            
    #     return ans



        
# @lc code=end

