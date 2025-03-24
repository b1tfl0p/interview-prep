from collections import deque
from typing import Self, final


@final
class TreeNode:
    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(level_order: list[int | None]):
    if not level_order or level_order[0] is None:
        return TreeNode(0)

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        if i < len(level_order) and (val := level_order[i]) is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        i += 1

        if i < len(level_order) and (val := level_order[i]) is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
        i += 1

    return root

