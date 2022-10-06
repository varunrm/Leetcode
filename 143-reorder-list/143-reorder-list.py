# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        fast=self.reverse(slow.next)
        slow.next=None
        slow=head
        temp=slow.next
        while fast !=None:
            slow.next =fast
            fast=fast.next
            slow.next.next=temp
            slow=temp
            if (temp!=None):
                temp=temp.next
    def reverse(self,head):
        if head==None or head.next==None:
            return head
        prev=None
        curr=head
        fast=head.next
        while fast!=None:
            curr.next=prev
            prev=curr
            curr=fast
            fast=fast.next
        curr.next=prev
        return curr