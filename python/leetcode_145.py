# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:  # 递归
        def post_order(root):
            if not root:
                return res
            post_order(root.left)
            post_order(root.right)
            res.append(root.val)
        res = list()
        post_order(root)
        return res

    def postorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:  # 迭代
        res = list()
        if not root:
            return res
        stack = []
        node = root
        pre = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == pre:
                res.append(node.val)
                pre = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return res

    def postorderTraversal3(self, root: Optional[TreeNode]) -> list[int]:  # Morris
        pass