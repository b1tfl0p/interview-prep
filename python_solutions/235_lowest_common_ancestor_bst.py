from typing import final


@final
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class RecursiveSolution:
    """
    Time complexity: O(h)
    Space complexity: O(h)
    where "h" is the height of the tree
    """

    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        if not root or not p or not q:
            return None
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


class IterativeSolution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        while root:
            if root.val < min(p.val, q.val):
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root


# My original answer:
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if (
            (root.val == p.val or root.val == q.val)
            or (p.val < root.val and root.val < q.val)
            or (q.val < root.val and root.val < p.val)
        ):
            return root
        if p.val < root.val and q.val < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)

        # Unreachable:
        return root
