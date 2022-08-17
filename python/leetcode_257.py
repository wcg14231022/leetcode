# Definition for a binary tree node.
import collections
import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:  # 深度优先
        res_list = list()
        temp_list = ""

        def dfs(root, temp_list):
            temp_list += "->{}".format(root.val)
            if not root.left and not root.right:
                res_list.append(temp_list[2:])
                return
            cur = temp_list
            if root.left:
                dfs(root.left, temp_list)
            temp_list = cur
            if root.right:
                dfs(root.right, temp_list)
            return

        dfs(root, temp_list)
        return res_list

    def binaryTreePaths2(self, root: Optional[TreeNode]) -> list[str]:  # 广度优先
        paths = list()
        if not root:
            return paths
        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])
        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + "->" + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + "->" + str(node.right.val))
        return paths


# 根据层序遍历序列生成二叉树
def creat_bin_tree(nums: list[str]) -> TreeNode:
    length = len(nums)
    my_que = collections.deque()
    root = TreeNode(int(nums[0]), None, None)
    my_que.append(root)
    ptr = root
    index = 1
    while my_que and index < length:
        cur_node = my_que.popleft()
        if index < length:
            if nums[index]:
                new_node = TreeNode(int(nums[index]))
            else:
                new_node = None
            cur_node.left = new_node
            my_que.append(new_node)
            index += 1
        if index < length:
            if nums[index]:
                new_node = TreeNode(int(nums[index]))
            else:
                new_node = None
            cur_node.right = new_node
            my_que.append(new_node)
            index += 1
    return ptr

my_tree = creat_bin_tree([1,2,3,None,5])

solution = Solution()
print(solution.binaryTreePaths(my_tree))

