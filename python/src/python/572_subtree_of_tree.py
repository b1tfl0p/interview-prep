from typing import Self, final


@final
class TreeNode:
    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# DFS:
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        return self.isSameTree(root, subRoot) or (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
                root.right, subRoot.right
            )

        return False


# Serialization & Pattern Matching:
class Solution2:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)

        return serialized_subRoot in serialized_root

    def serialize(self, node: TreeNode | None) -> str:
        if not node:
            return "N"
        return f"({node.val},{self.serialize(node.left)},{self.serialize(node.right)})"
