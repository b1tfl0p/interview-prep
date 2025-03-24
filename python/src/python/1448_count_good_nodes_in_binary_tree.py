import pytest

from helpers.tree_builder import build_binary_tree, TreeNode


class Solution:
    def helper(self, node: TreeNode, max_parent: int) -> int:
        count = 0
        if node.val >= max_parent:
            count += 1
        max_parent = max(node.val, max_parent)
        if node.left:
            count += self.helper(node.left, max_parent)
        if node.right:
            count += self.helper(node.right, max_parent)
        return count

    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        if root.left:
            count += self.helper(root.left, root.val)
        if root.right:
            count += self.helper(root.right, root.val)
        return count


@pytest.mark.parameterize(
    "input, answer",
    [
        ([1], 1),
        ([3, 1, 4, 3, None, 1, 5], 4),
    ],
)
def test_solution(input: list[int | None], answer: int):
    root: TreeNode = build_binary_tree(input)
    assert Solution().goodNodes(root) == answer
