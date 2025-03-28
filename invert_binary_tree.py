from collections import deque
from enum import Enum
from typing import Self, final


@final
class TreeNode:
    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


@final
class Traverse(Enum):
    BFS = 1
    DFS = 2
    ITERATIVE_DFS = 3


class Solution:
    def invertTree(self, root: TreeNode | None, traverse: Traverse) -> TreeNode | None:
        match traverse:
            case Traverse.BFS:
                return self.bfs(root)
            case Traverse.DFS:
                return self.dfs(root)
            case Traverse.ITERATIVE_DFS:
                return self.iterative_dfs(root)

    def bfs(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        queue: deque[TreeNode] = deque([root])
        while queue:
            curr: TreeNode = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root

    def dfs(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        root.left, root.right = self.dfs(root.right), self.dfs(root.left)
        return root

    def iterative_dfs(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
