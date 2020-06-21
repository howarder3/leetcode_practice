#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val: #init header
            head = ans = ListNode(l1.val)
            l1 = l1.next  

        else: #init header
            head = ans = ListNode(l2.val)
            l2 = l2.next  

        while(l1 or l2):
            if not l1:
                ans.next = l2
                return head
            if not l2:
                ans.next = l1
                return head
                
            if l1.val <= l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next   
            else:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next

        return head
        
# @lc code=end

