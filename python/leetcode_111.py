# Definition for a binary tree node.
import collections
import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:  # 层序遍历
        if not root:
            return 0
        que = queue.Queue()
        que.put(root)
        depth = 0
        while not que.empty():
            cur_length = que.qsize()
            if cur_length > 0:
                depth += 1
            for i in range(cur_length):
                node = que.get()
                if node:
                    if not node.left and not node.right:
                        return depth
                    que.put(node.left)
                    que.put(node.right)
        return depth

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return 0