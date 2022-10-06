# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA,lB=0,0
        curr=headA
        while curr!= None:
            curr=curr.next
            lA+=1
        curr=headB
        while curr!= None:
            curr=curr.next
            lB+=1
        while lA<lB :
            headB=headB.next
            lB=lB-1
        while lB<lA:
            headA=headA.next
            lA-=1
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA