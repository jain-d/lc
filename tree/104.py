# Maxium Depth of Binary Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

class Solution:
    def max_depth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left_height = 1 + self.max_depth(root.left)
        right_height = 1 + self.max_depth(root.right)

        return left_height if left_height > right_height else right_height
