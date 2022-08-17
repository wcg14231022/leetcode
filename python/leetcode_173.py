# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder_arr = list()
        self.index = -1
        def reverse(root):
            if not root:
                return
            reverse(root.left)
            self.inorder_arr.append(root.val)
            reverse(root.right)
        reverse(root)

    def next(self) -> int:
        self.index += 1
        return self.inorder_arr[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.inorder_arr) - 1



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()