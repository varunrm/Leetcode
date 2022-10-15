# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first=None
        curr=head
        #1->2->3->4->5
        while curr:
            n=curr.next #2-3-4-5
            curr.next=first# 1-0
            first=curr#1-0
            curr=n #2-3-4-5
        head=first
        return head
            
            
            