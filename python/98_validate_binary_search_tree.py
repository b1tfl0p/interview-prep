from collections import deque
from helpers.binary_tree import TreeNode, build_binary_tree
import pytest


class DfsSolution:
    """
    T: O(n)
    S: O(n)
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid(
            node: TreeNode | None, left: int | float, right: int | float
        ) -> bool:
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return is_valid(node.left, left, node.val) and is_valid(
                node.right, node.val, right
            )

        return is_valid(root, float("-inf"), float("inf"))


class BfsSolution:
    """
    T: O(n)
    S: O(n)
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if not (left < node.val < right):
                return False

            if node.left:
                q.append((node.left, left, node.val))

            if node.right:
                q.append((node.right, node.val, right))

        return True


@pytest.mark.parametrize(
    "nodes, answer",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
    ],
)
def test_solutions(nodes: list[int | None], answer: bool):
    t = build_binary_tree(nodes)

    assert DfsSolution().isValidBST(t) == answer
    assert BfsSolution().isValidBST(t) == answer
