# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge(list1, list2)

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2


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


l1 = [1, 2, 4]
l2 = [1, 3, 4]
link_list_1 = creat_link_list(l1)
link_list_2 = creat_link_list(l2)

solution = Solution()
print_link_list(solution.mergeTwoLists(link_list_1, link_list_2))
