# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:  # 递归
        def pre_order(root):
            if not root:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)
        res = list()
        pre_order(root)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:  # 层序
        res = list()
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def preorderTraversal3(self, root: Optional[TreeNode]) -> list[int]:  # Morris
        res = list()
        if not root:
            return res
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right
        return res