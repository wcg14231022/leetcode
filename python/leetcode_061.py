# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = self.get_link_list_length(head)
        mod = k % length
        if mod == 0:
            return head
        move = length - mod
        ptr = head
        for i in range(move - 1):
            ptr = ptr.next
        new_head = ptr.next
        ptr.next = None
        ptr = new_head
        while ptr:
            if not ptr.next:
                ptr.next = head
                break
            ptr = ptr.next
        return new_head

    def get_link_list_length(self, list: ListNode):
        length = 0
        while list:
            length += 1
            list = list.next
        return length

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


nums = [1,2]
link_list = creat_link_list(nums)

solution = Solution()
link_list = solution.rotateRight(link_list, 2)
print_link_list(link_list)