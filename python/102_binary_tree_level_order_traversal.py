from helpers import binary_tree


class Solution:
    def levelOrder(self, root: binary_tree.TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res: list[list[int]] = []
        q = [root]
        vals: list[int] = []
        next_q: list[binary_tree.TreeNode] = []
        while q:
            for node in q:
                vals.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.append(vals)
            q, vals, next_q = next_q, [], []

        return res
