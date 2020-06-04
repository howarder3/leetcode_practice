#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    def sortedListToBST(self, head):
        if head is None:
            return None

        val_arr = []
        # linked list to array
        while(head):
            val_arr.append(head.val)
            head = head.next

        # print(val_arr)

        return self.buildBST(val_arr)

        

    def buildBST(self, val_arr):
        if not val_arr:
            return None

        idx = len(val_arr)//2
        root = TreeNode(val_arr[idx])
        root.left = self.buildBST(val_arr[:idx])
        root.right = self.buildBST(val_arr[idx+1:])

        return root




        
# @lc code=end

