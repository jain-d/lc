# Same Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p and q:
            if p.val == q.val:
                left_check = self.is_same_tree(p.left, q.left)
                right_check = self.is_same_tree(p.right, q.right)
                return left_check and right_check

        elif p is q:
            return True
        return False
