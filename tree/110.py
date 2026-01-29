# Balanced Binary Tree
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    val: int = 0
    left: Node | None = None
    right: Node | None = None

class Solution:
    def is_balanced(self, root: Node | None) -> bool:
        if not root:
            return True
        try:
            left = self._depth_calculator(root.left) if root.left else 0
            right = self._depth_calculator(root.right) if root.right else 0
        except:
            return False

        return True if abs(left - right) <= 1 else False

    def _depth_calculator(self, node: Node) -> int:
        left: int = 0
        right: int = 0
        if node.left:
            left += self._depth_calculator(node.left) 
        if node.right:
            right += self._depth_calculator(node.right)
        
        if abs(left - right) > 1:
            raise Exception()

        return max(left, right) + 1

solution = Solution()

tree_one = Node(3, Node(9), Node(20, Node(15), Node(7)))
tree_two = Node(1, Node(2, Node(3, Node(4), Node(4)), Node(3)), Node(2))
tree_three = None
tree_four = Node(1, Node(2, Node(3, Node(4))), Node(2, None, Node(3, None, Node(4))))
tree_five = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6, Node(7))))

trees = ((tree_one, True), (tree_two, False), (tree_three, True), (tree_four, False), (tree_five, False))
for tree in trees:
    if solution.is_balanced(tree[0]) == tree[1]:
        print("\033[32mPASS\033[0m")
    else:
        print("\033[31mFAIL\033[0m")
