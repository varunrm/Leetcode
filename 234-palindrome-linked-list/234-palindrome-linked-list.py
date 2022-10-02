# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        ll=head
        i=0
        while ll:
            stack.append(ll.val)
            ll=ll.next
        while head:
            if head.val != stack.pop():
                return False
            head=head.next
        return True
