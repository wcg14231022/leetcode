# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  # 一次遍历
        ancestor = root
        while True:
             if p.val < ancestor.val and q.val < ancestor.val:
                 ancestor = ancestor.left
             elif p.val > ancestor.val and q.val > ancestor.val:
                 ancestor = ancestor.right
             else:
                 break
        return ancestor

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  # 两次遍历
        def get_path(root: TreeNode, target: TreeNode) -> list[TreeNode]:
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path_p = get_path(root, p)
        path_q = get_path(root, q)
        ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor