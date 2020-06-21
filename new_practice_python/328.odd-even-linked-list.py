#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Clear Python Solution
# https://leetcode.com/problems/odd-even-linked-list/discuss/78095/Clear-Python-Solution

# : ListNode) -> ListNode:
class Solution:
    # def oddEvenList(self, head):
    #     odd_list = p1 = ListNode(0) # odd_list 做頭, p1當移動指標
    #     # print(odd_list) #1
    #     even_list = p2 = ListNode(0) # even_list 做頭, p2當移動指標
    #     # print(even_list) #2
        
    #     # print(out_list) #1
    #     d1 = head


    #     while(True):
    #         if head: # odd
    #             # print(head)
    #             p1.next = head #不改掉自己的0 -> 下一個從1開始
    #             # print(p1)
    #             p1 = p1.next #移動指標
    #             head = head.next
    #         else:
    #             p1.next = None
    #             break

    #         if head: #even
    #             # print(head)
    #             p2.next = head #不改掉自己的0 -> 下一個從2開始
    #             # print(p2)
    #             p2 = p2.next #移動指標
    #             head = head.next
    #         else:
    #             p2.next = None
    #             break

    #     # print(odd_list)  
    #     # print(even_list)
    #     p1.next = even_list.next  #從自己的0下一個開始
    #     # print(odd_list)

    #     return odd_list.next #從自己的0下一個開始
        
        

#     def oddEvenList(self, head):
    #     dummy1 = odd = ListNode(0) #一個當頭一個移動指標
        # dummy2 = even = ListNode(0) #一個當頭一個移動指標
        # while head:
        #     odd.next = head #從0的下一個開始塞資料
        #     even.next = head.next  #從0的下一個開始塞資料
        #     odd = odd.next #移動指標
        #     even = even.next #移動指標
        #     head = head.next.next if even else None #移動指標

        # odd.next = dummy2.next #接起來 奇數尾巴 接 偶數頭
        # return dummy1.next

    # class Solution(object):
        # def oddEvenList(self, head):
        # """
        # :type head: ListNode
        # :rtype: ListNode
        # """
        # d1=odd=ListNode(0)
        # d2=even=ListNode(0)
        # i=1
        # while head:
        #     if i%2: # 有餘數是奇數
        #         odd.next,odd=head,head # 先移"此處oddnext"指的東西, 再移"移動指標odd"
        #     else: # 偶數
        #         even.next,even=head,head

        #     head=head.next
        #     i+=1
        # odd.next,even.next=d2.next,None
        # return d1.next

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# With detailed explanation | Python
# https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next # 移動next指的東西
            even.next = even.next.next # 移動next指的東西
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next # 移動動態指標
            even = even.next # 移動動態指標
        
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        
        return head # We keep the start of the odd-node list in the first of our code
        
# @lc code=end

