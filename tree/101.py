# Symmetric Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            return self.is_mirror(root.left, root.right)
        else:
            return False

    def is_mirror(self, left: TreeNode | None,  right: TreeNode | None) -> bool:
        if left and right:
            if left.val == right.val:
                one_side = self.is_mirror(left.right, right.left)
                another_side = self.is_mirror(left.left, right.right)
                return one_side and another_side
        elif left is right:
            return True
        return False

root_one = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
solution = Solution()
print(solution.is_symmetric(root_one))
