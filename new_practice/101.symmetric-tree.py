#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def isSymmetric(self, root: TreeNode) -> bool:

# https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python
# sol recursively
# class Solution:
#     def isSymmetric(self, root):
#         if not root: # nothing
#             return True
#         else:
#             return self.isMirror(root.left, root.right)


#     def isMirror(self, l, r):
#         if l is None and r is None: # both side none
#             return True
#         if l is None or r is None: # only one side none
#             return False

#         if l.val == r.val: # same value
#             out_compare = self.isMirror(l.left, r.right)
#             in_compare = self.isMirror(l.right, r.left)
#             return out_compare and in_compare
#         else:
#             return False # not same value


# sol iteratively
# class Solution:
#     def isSymmetric(self, root):
#         if root is None:
#             return True

#         stack = [[root.left, root.right]]

#         while len(stack) > 0:
#             pair = stack.pop()
#             l = pair[0]
#             r = pair[1]

#             if l is None and r is None:
#                 continue
#             if l is None or r is None:
#                 return False

#             if l.val == r.val:
#                 stack.insert(0, [l.left , r.right])
#                 stack.insert(0, [l.right, r.left])
#             else:
#                 return False

#         return True



class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop()
            l = pair[0]
            r = pair[1]

            # check if nothing
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False

            # append next pair
            if l.val == r.val:
                stack.append([l.left , r.right])
                stack.append([l.right, r.left])
            else:
                return False

        return True

        

        
# @lc code=end

