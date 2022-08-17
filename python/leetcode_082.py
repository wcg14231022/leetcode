# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or (head and not head.next):
            return head
        pre = ListNode(None, head)
        ptr = pre
        while ptr.next and ptr.next.next:
            if ptr.next.val == ptr.next.next.val:
                temp = ptr.next.next
                while temp and temp.val == ptr.next.val:
                    temp = temp.next
                ptr.next = temp
            else:
                ptr = ptr.next
        return pre.next

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

link_list = creat_link_list([1,1])
solution = Solution()
print_link_list(solution.deleteDuplicates(link_list))