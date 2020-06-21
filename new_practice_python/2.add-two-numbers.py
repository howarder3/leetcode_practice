#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# self, l1: ListNode, l2: ListNode) -> ListNode:


# https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward

class Solution:
    def addTwoNumbers(self, l1, l2):

        carry = 0
        root = temp = ListNode(0)

        while l1 or l2 or carry: # something left
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            carry, val = divmod(carry+val1+val2, 10)
            temp.next = ListNode(val) # add new node 
            temp = temp.next

        return root.next


        # head = l1
        # flag = 0

        # while(True):
        #     if not l1:
        #         if l2:
        #             if flag == 1:
        #                 l2.val = l2.val + 1
        #                 l1 = l2
        #                 return head
        #             else:
        #                 head.next = l2
        #                 return head
        #         else: # no l2 
        #             if flag == 1:
        #                 head.next = ListNode(1)
        #                 return head
        #             else:
        #                 return head

        #     if not l2:
        #         if flag == 1:
        #             l1.val = l1.val + 1
        #             return head
        #         else:
        #             return head

        #     l1.val  = l1.val + l2.val + flag
        #     if l1.val >= 10:
        #         l1.val = l1.val - 10 
        #         flag = 1
        #     else:
        #         flag = 0
                
        #     l1 = l1.next
        #     l2 = l2.next
        



        # return 




        
# @lc code=end

