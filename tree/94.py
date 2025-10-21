# Binary Tree Inorder Traversal
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def inorder_traversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        inorder_list = self.inorder_traversal(root.left)
        inorder_list.append(root.val)
        inorder_list.extend(self.inorder_traversal(root.right))

        return inorder_list
