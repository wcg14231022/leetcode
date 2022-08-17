# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:  # 自顶向下递归解法
        if not root:
            return True
        if abs(self.get_tree_height(root.left) - self.get_tree_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_tree_height(self, root):
        if not root:
            return 0
        return max(self.get_tree_height(root.left) + 1, self.get_tree_height(root.right) + 1)

    def isBalanced2(self, root: TreeNode) -> bool:  # 自底向上递归解法
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1
        return height(root) >= 0

