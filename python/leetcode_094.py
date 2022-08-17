# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:  # 递归遍历
        self.inorder_arr = list()
        self.inorder(root)
        return self.inorder_arr

    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.inorder_arr.append(root.val)
        if root.right:
            self.inorder(root.right)
        return

    def inorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:  # 非递归遍历
        self.unrevers_inorder_arr = list()
        if not root:
            return self.unrevers_inorder_arr
        node_stack = list()
        while node_stack or root:
            while root:
                node_stack.insert(0, root)
                root = root.left
            root = node_stack[0]
            self.unrevers_inorder_arr.append(root.val)
            node_stack.pop(0)
            root = root.right
        return self.unrevers_inorder_arr

    def inorderTraversal3(self, root: Optional[TreeNode]) -> list[int]:  # Morris遍历
        self.morris_arr = list()
        morris_ptr = TreeNode()
        while root:
            if root.left:
                morris_ptr = root.left
                while morris_ptr.right and morris_ptr.right != root:
                    morris_ptr = morris_ptr.right
                if not morris_ptr.right:
                    morris_ptr.right = root
                    root = root.left
                else:
                    self.morris_arr.append(root.val)
                    morris_ptr = None
                    root = root.right
            else:
                self.morris_arr.append(root.val)
                root = root.right
        return self.morris_arr

node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(3, None, None)
node1.right = node2
node2.left = node3

solution = Solution()
print(solution.inorderTraversal3(node1))