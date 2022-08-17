# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        fast = head.next
        while fast:
            if fast.val != pre.val:
                pre.next.val = fast.val
                pre = pre.next
            fast = fast.next
        pre.next = None
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head or (head and not head.next):
            return head
        ptr = head
        while ptr:
            while ptr.next and ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return head

def creat_link_list(nums: list) -> ListNode:
    node = ListNode()
    for index in range(len(nums) - 1, -1, -1):
        node_a = ListNode(nums[index], node.next)
        node.next = node_a
    return node.next

def print_link_list(link_list):
    if not link_list:
        print("NULL")
    while link_list:
        print(link_list.val)
        link_list = link_list.next

link_list = creat_link_list([1,1,1])
solution = Solution()
print_link_list(solution.deleteDuplicates(link_list))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
link_list = creat_link_list([1,1,1])
print_link_list(solution.deleteDuplicates2(link_list))