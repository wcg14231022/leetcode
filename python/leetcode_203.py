# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements1(self, head: ListNode, val: int) -> ListNode:  # 迭代
        pre = ListNode(None, head)
        pivot = pre
        while pre and pre.next:
            while pre.next and pre.next.val == val:
                pre.next = pre.next.next
            pre = pre.next
        return pivot.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:  # 递归
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head