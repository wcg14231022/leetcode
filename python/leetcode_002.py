# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        return
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.recursive(l1, l2, 0)

    def recursive(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        numa = l1.val if l1 else 0
        numb = l2.val if l2 else 0
        num = (numa + numb + carry) % 10
        carry = int((numa + numb + carry) / 10)
        if not l1 and not l2:
            return None if num == 0 else ListNode(num, None)
        if l1 and l2:
            return ListNode(num, self.recursive(l1.next, l2.next, carry))
        return ListNode(num, self.recursive(l1.next, None, carry)) if not l2 else ListNode(num, self.recursive(None, l2.next, carry))


def creat_link_list(nums: list) -> ListNode:
    node = ListNode()
    for index in range(len(nums) - 1, -1, -1):
        node_a = ListNode(nums[index], node.next)
        node.next = node_a
    return node.next


arr_1 = [9, 9, 9, 9, 9, 9, 9]
arr_2 = [9, 9, 9, 9]

link_list_1 = creat_link_list(arr_1)
link_list_2 = creat_link_list(arr_2)
solution = Solution()
node = solution.addTwoNumbers(link_list_1, link_list_2)
print(node)