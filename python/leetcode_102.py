# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res_arr = list(list())
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            temp_arr = list()
            num_arr = list()
            while not que.empty():
                node = que.get()
                if node:
                    temp_arr.append(node)
                    num_arr.append(node.val)
            if num_arr:
                res_arr.append(num_arr)
            for nodes in temp_arr:
                que.put(nodes.left)
                que.put(nodes.right)
        return res_arr

    def levelOrder2(self, root: TreeNode) -> list[list[int]]:
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
        return res_arr

root = TreeNode(3, None, None)
node_9 = TreeNode(9, None, None)
node_20 = TreeNode(20, None, None)
node_15 = TreeNode(15, None, None)
node_7 = TreeNode(7, None, None)
root.left = node_9
root.right = node_20
node_20.left = node_15
node_20.right = node_7

solution = Solution()
print(solution.levelOrder(root))
print(solution.levelOrder2(root))
