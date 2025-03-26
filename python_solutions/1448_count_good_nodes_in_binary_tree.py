from collections import deque
import pytest

from helpers.binary_tree import build_binary_tree, TreeNode


class BfsSolution:
    """
    T: O(n)
    S: O(n)
    """

    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, float("-inf")))

        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                res += 1

            if node.left:
                q.append((node.left, max(max_val, node.val)))

            if node.right:
                q.append((node.right, max(max_val, node.val)))

        return res


class DfsSolution:
    """
    T: O(n)
    S: O(n)
    """

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, max_val: int) -> int:
            if not node:
                return 0

            if node.val >= max_val:
                count = 1
                max_val = node.val
            else:
                count = 0

            return count + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)


@pytest.mark.parametrize(
    "input, answer",
    [
        ([1], 1),
        ([3, 1, 4, 3, None, 1, 5], 4),
    ],
)
def test_solution(input: list[int | None], answer: int):
    root: TreeNode = build_binary_tree(input)
    assert DfsSolution().goodNodes(root) == answer
    assert BfsSolution().goodNodes(root) == answer
