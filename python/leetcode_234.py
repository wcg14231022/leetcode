# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:  # 先遍历再判断
        node_list = list()
        while head:
            node_list.append(head.val)
            head = head.next
        length = len(node_list)
        if length == 1:
            return True
        left, right = 0, length - 1
        while left < right:
            if node_list[left] != node_list[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, head: ListNode) -> bool:  # 递归
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

    def isPalindrome3(self, head: ListNode) -> bool:  # 快慢指针，反转后半部分
        if not head:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next

        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
