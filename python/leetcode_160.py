# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptrA = headA
        ptrB = headB
        while ptrA != ptrB:
            if not ptrA:
                ptrA = headB
            else:
                ptrA = ptrA.next
            if not ptrB:
                ptrB = headA
            else:
                ptrB = ptrB.next
        return ptrA