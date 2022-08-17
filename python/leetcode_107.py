# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        res_arr = list(list())
        if not root:
            return res_arr
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            temp_arr = list()
            cur_length = que.qsize()
            for i in range(cur_length):
                node = que.get()
                if node:
                    temp_arr.append(node.val)
                    que.put(node.left)
                    que.put(node.right)
            if temp_arr:
                res_arr.append(temp_arr)
        return res_arr[::-1]