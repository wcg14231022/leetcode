# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:  # 头插法
        new_head = ListNode()
        ptr = head
        while ptr:
            temp = ptr
            ptr = ptr.next
            temp.next = new_head.next
            new_head.next = temp
        return new_head.next

    def reverseList2(self, head: ListNode) -> ListNode:  # 递归
        if not head or not head.next:
            return head
        new_head = ListNode()
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head