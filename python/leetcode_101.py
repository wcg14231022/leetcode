# Definition for a binary tree node.
import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:  # 递归解法
        if not root:
            return True
        return self.symmetric_tree(root.left, root.right)

    def symmetric_tree(self, left_tree, right_tree) -> bool:
        if not left_tree and not right_tree:
            return True
        if not left_tree or not right_tree:
            return False
        if left_tree.val != right_tree.val:
            return False
        return self.symmetric_tree(left_tree.left, right_tree.right) and self.symmetric_tree(left_tree.right, right_tree.left)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:  # 迭代解法
        return self.symmetric_tree2(root, root)

    def symmetric_tree2(self, left_tree, right_tree) -> bool:
        q = queue.Queue()
        q.put(left_tree)
        q.put(right_tree)
        while q:
            a_tree = q.get()
            b_tree = q.get()
            if not a_tree and not b_tree:
                continue
            if (not a_tree or not b_tree) or (a_tree.val != b_tree.val):
                return False
            q.put(a_tree.left)
            q.put(b_tree.right)
            q.put(a_tree.right)
            q.put(b_tree.left)
        return True