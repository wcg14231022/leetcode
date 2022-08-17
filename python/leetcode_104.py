# Definition for a binary tree node.
import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # 深度优先
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

    def maxDepth2(self, root: Optional[TreeNode]) -> int:  # 广度优先
        que = queue.Queue()
        if not root:
            return 0
        depth = 0
        que.put(root)
        while not que.empty():
            depth += 1
            cur_length = que.qsize()
            for i in range(cur_length):
                node = que.get()
                if node:
                    if node.left:
                        que.put(node.left)
                    if node.right:
                        que.put(node.right)
        return depth