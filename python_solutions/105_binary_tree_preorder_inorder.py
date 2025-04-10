from helpers.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        indicies = {val: i for i, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            nonlocal pre_idx
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = indicies[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
