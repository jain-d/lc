# Balanced Binary Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

class Solution:
    def is_balanced(self, root: TreeNode | None) -> bool:
        if root:
            left_height = self.height(root.left) if root.left else 0
            right_height = self.height(root.right) if root.right else 0
            difference = abs(left_height - right_height)
            if difference < 2:
                return True
            else:
                return False
        else:
            return True
    
    def height(self, tree: TreeNode) -> int:
        left_height: int
        right_height: int

        left_height = (self.height(tree.left) + 1) if tree.left else 0
        right_height = (self.height(tree.right) + 1) if tree.right else 0

        return max(left_height, right_height)


solution = Solution()

tree_one = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree_two = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
tree_three = None

trees = ((tree_one, True), (tree_two, False), (tree_three, True))

for tree in trees:
    if not (solution.is_balanced(tree[0]) ^ tree[1]):
        print("\033[32mPASS\033[0m")
    else:
        print("\033[31mFAIL\033[0m")
