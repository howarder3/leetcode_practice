#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # def connect(self, root: 'Node') -> 'Node':
    def connect(self, root):
        if not root:
            return 
            
        level = [root]

        while level:
            for idx in range(0, len(level)-1):
                level[idx].next = level[idx+1]

            level[-1].next = None

            next_level = []
            for ele in level:
                if ele.left is not None:
                    next_level.append(ele.left)
                if ele.right is not None:
                    next_level.append(ele.right)

            level = next_level

        return root
        
# @lc code=end

