# Iterative Binary tree traversal using a stack
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def tree_traversal_through_stack(root: TreeNode | None):
    traversal_stack: list[TreeNode] = []
    if root:
        traversal_stack.append(root)
        left_removed: TreeNode | None = None
        right_removed: TreeNode | None = None
    while traversal_stack:
        current_node = traversal_stack[-1]

        if current_node.left and left_removed is not current_node.left:
            traversal_stack.append(current_node.left)
        elif current_node.right and right_removed is not current_node.right:
            traversal_stack.append(current_node.right)
        else:
            print(current_node.val)
            last_removed = traversal_stack.pop()
            if traversal_stack and last_removed is traversal_stack[-1].left:
                left_removed = last_removed
            else:
                right_removed = last_removed



tree_zero = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree_one = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))

tree_traversal_through_stack(tree_one)
