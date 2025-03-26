import pytest
from helpers.binary_tree import TreeNode, build_binary_tree


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        max_sum = root.val

        def dfs(root: TreeNode | None) -> int:
            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            nonlocal max_sum
            max_sum = max(max_sum, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        _ = dfs(root)
        return max_sum


@pytest.mark.parametrize(
    "input, answer", [([1, 2, 3], 6), ([-15, 10, 20, None, None, 15, 5, -5], 40)]
)
def test_solution(input: list[int | None], answer: int):
    root = build_binary_tree(input)
    assert Solution().maxPathSum(root) == answer
