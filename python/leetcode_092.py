# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:  # 两次遍历解法
        pre = ListNode(None, head)
        count_index = 0
        ptr = pre
        node_arr = []
        start_node = ListNode()
        end_node = ListNode()
        while ptr:
            if count_index == left - 1:
                start_node = ptr
            if count_index == right:
                end_node = ptr.next
            ptr = ptr.next
            count_index += 1
            if left <= count_index <= right:
                node_arr.append(ptr)
        start_next, end_pre = self.creat_link_list_reverse(node_arr)
        start_node.next = start_next
        end_pre.next = end_node
        return pre.next

    def creat_link_list_reverse(self, nodes):
        head = ListNode()
        tail_node = ListNode
        head_node = ListNode
        for index in range(len(nodes)):
            if index == 0:
                tail_node = nodes[index]
            if index == len(nodes) - 1:
                head_node = nodes[index]
            nodes[index].next = head.next
            head.next = nodes[index]
        return head_node, tail_node

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:  # 一次遍历解法
        pre_node = ListNode(None, head)
        pre_start = pre_node
        index_count = 0
        pre_start_flag = False
        while head:
            index_count += 1
            if index_count + 1 == left and not pre_start_flag:
                pre_start = head
                pre_start_flag = True
            if index_count == left and not pre_start_flag:
                pre_start_flag = True
            if left <= index_count < right:
                temp = head.next
                head.next = head.next.next
                temp.next = pre_start.next
                pre_start.next = temp
            else:
                head = head.next
            if not pre_start_flag:
                pre_start = pre_start.next
        return pre_node.next

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

solution = Solution()
test_link = creat_link_list([1,2,3,4,5])
res_link = solution.reverseBetween(test_link, 2, 4)
print_link_list(res_link)

print(">>>>>>>>>>>>>>>>>>")
test_link = creat_link_list([1,2,3])
res_link = solution.reverseBetween2(test_link, 1, 3)
print_link_list(res_link)